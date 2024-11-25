from flask import Flask, render_template, redirect, request, session
import multiprocessing
import webview
import hashing
import os
import secrets

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def root():
    # Check if the keys are generated
    if not os.path.isfile("keys/private.key") or not os.path.isfile("keys/public.key"):
        return redirect("/setup-key")

    # Check if the user is logged in by checking if the private key password is set
    if not "private_key_password" in session:
        return redirect("/login")

    return render_template("index.html")


@app.route("/setup-key", methods=["GET", "POST"])
def setupKey():
    if request.method == "POST":
        password = request.form.get("password")

        # TODO: implement password validation
        kp = hashing.KeyPair()

        kp.set_private_key_password(password)
        kp.generate_key_pair()
        kp.save_keys_to_files()

        return redirect("/")

    return render_template("setup-key.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        password = request.form.get("password")

        # Check if the password is correct by trying to load the key pair with the password
        kp = hashing.KeyPair()
        if kp.load_existing_key_pair(password):
            session["private_key_password"] = password
            return redirect("/")
        else:
            return redirect("/login")

    return render_template("login.html")


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html", error=error), 500


def start_webview():
    webview.create_window("Password Manager", app)
    webview.start()


if __name__ == "__main__":
    webview_process = multiprocessing.Process(target=start_webview)
    webview_process.start()

    app.run(debug=True, use_reloader=False)
