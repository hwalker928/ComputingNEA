from flask import Flask, render_template, redirect, request
import multiprocessing
import webview
import hashing
import os

app = Flask(__name__)


@app.route("/")
def root():
    if not os.path.isfile("keys/private.key") or not os.path.isfile("keys/public.key"):
        return redirect("/setup-key")

    # TODO: check if the user is logged in before redirecting to login page
    return redirect("/login")


@app.route("/setup-key", methods=["GET", "POST"])
def setupKey():
    if request.method == "POST":
        password = request.form.get("password")

        kp = hashing.KeyPair()

        kp.set_private_key_password(password)
        kp.generate_key_pair()
        kp.save_keys_to_files()

        return redirect("/")

    return render_template("setup-key.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


def start_webview():
    webview.create_window("Password Manager", app)
    webview.start()


if __name__ == "__main__":
    webview_process = multiprocessing.Process(target=start_webview)
    webview_process.start()

    app.run(debug=True, use_reloader=False)
