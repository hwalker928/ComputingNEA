from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def root():
    # TODO: check if the user is logged in before redirecting to login page
    return redirect("/login")


@app.route("/login")
def login_page():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
