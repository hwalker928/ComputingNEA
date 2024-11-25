from flask import Flask, render_template, redirect, request
import secrets
import multiprocessing
import webview

app = Flask(__name__)


@app.route("/")
def root():
    if app.secret_key is None:
        return redirect("/setup-key")

    # TODO: check if the user is logged in before redirecting to login page
    return redirect("/login")


@app.route("/setup-key", methods=["GET", "POST"])
def setupKey():
    if request.method == "POST":
        app.secret_key = secrets.token_urlsafe(16)
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
