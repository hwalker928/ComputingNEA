from flask import Flask, render_template, redirect, request, session, flash
import multiprocessing
import webview
import os
import secrets

from utils import encryption, validation, database

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = secrets.token_urlsafe(16)

# Initialize the database
database = database.Database("data/database.db")

# Reset the database to schema
database.setup_database()


@app.route("/")
def root():
    # Check if the keys are generated
    if not os.path.isfile("keys/private.key") or not os.path.isfile("keys/public.key"):
        return redirect("/setup-key")

    # Check if the user is logged in by checking if the private key password is set
    if not "private_key_password" in session:
        return redirect("/login")

    if not database.get_user_detail("name"):
        return redirect("/setup-name")

    return render_template("index.html", name=database.get_user_detail("name"))


@app.route("/setup-key", methods=["GET", "POST"])
def setupKey1():
    if request.method == "GET":
        return render_template(
            "setup-key.html", entry_num=session.get("setup-key_setup_num", 1)
        )

    # Get the password from the form
    password = request.form.get("password")

    # Save the password to the session and redirect the user to confirm again
    if session.get("setup-key_setup_num", 1) == 1:
        # Check if the password passes validation
        valid, error = validation.check_valid_private_key_password(password)
        if not valid:
            # Return an error to the user if the password is weak
            flash(error, "error")
            return redirect("/setup-key")

        # Save the password to the session
        session["private_key_password"] = password
        session["setup-key_setup_num"] = 2
        session["show_password_requirements"] = False
        return redirect("/setup-key")

    # Check if the password matches the one saved in the session
    if password != session.get("private_key_password", ""):
        flash("Passwords do not match", "error")
        session["setup-key_setup_num"] = 1
        session["show_password_requirements"] = True
        return redirect("/setup-key")

    # Clear the password from the session as it is no longer needed
    session.pop("private_key_password", None)

    # Generate the key pair and save it locally
    kp = encryption.KeyPair()
    kp.set_private_key_password(password)
    kp.generate_key_pair()
    kp.save_keys_to_files()

    # Redirect the user to the stage 2 page after the key pair is generated
    return redirect("/setup-name")


@app.route("/setup-name", methods=["GET", "POST"])
def setupName2():
    if request.method == "GET":
        # TODO: make setup-name.html
        return render_template("setup-name.html")

    # Get the user's name from the form
    name = request.form.get("name")

    # Check if the name passes validation
    # TODO: this
    # valid, error = validation.check_valid_private_key_password(name)
    valid, error = True, None
    if not valid:
        # Return an error to the user if the name input is invalid
        flash(error, "error")
        return redirect("/setup-name")

    # Save the name to the database
    database.set_user_detail("name", name)

    # Redirect the user to the login page after the name is saved
    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")

    if session.get("login_attempts", 0) == -1:
        flash("Too many login attempts, please try again later", "error")

        return redirect("/login")

    # Get the password from the form
    password = request.form.get("password")

    # Check if the password is correct by trying to load the key pair with the password
    kp = encryption.KeyPair()
    if kp.load_existing_key_pair(password):
        # Password is valid
        session["private_key_password"] = password
        return redirect("/")

    # Increase the login attempts counter
    session["login_attempts"] = session.get("login_attempts", 0) + 1

    if session.get("login_attempts") == 3:
        # Too many login attempts, lock the user out
        session["login_attempts"] = -1
        flash("Too many login attempts, please try again later", "error")

        return redirect("/login")

    # Password is invalid, return an error
    flash(f"Invalid password, attempt {session.get('login_attempts')}/3", "error")

    return redirect("/login")


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html", error=error), 500


def start_webview():
    webview.create_window("Password Manager", app, confirm_close=True)
    webview.start()


if __name__ == "__main__":
    webview_process = multiprocessing.Process(target=start_webview)
    webview_process.start()

    try:
        app.run(debug=True, use_reloader=False)
    except KeyboardInterrupt:
        pass
