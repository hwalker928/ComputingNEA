from flask import Flask, render_template, redirect, request
import secrets

app = Flask(__name__)


@app.route("/")
def root():
    if app.secret_key is None:
        return redirect("/setup-key")

    # TODO: check if the user is logged in before redirecting to login page
    return redirect("/login")

@app.route("/setup-key", methods=['GET', 'POST'])
def setupKey():
    if request.method == 'POST':
        app.secret_key = secrets.token_urlsafe(16)
        return redirect("/")

    return render_template("setup.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


if __name__ == "__main__":
    # TODO: reset this to False before deploying
    app.run(debug=True)
