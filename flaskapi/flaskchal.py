from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)




@app.route("/user/<name>")
def user_page(name):
   return f"Hello {name}"

@app.route("/invalid")
def invalid_page():
   return f"You can't do that"

@app.route("/login")
def default(catch): 
   return redirect(url_for("user_page", name=catch))

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("loginid"):
            user = request.form.get("loginid")
        else:
            user = "defaultuser"

    return redirect(url_for("success", name = user))

@app.route("/")
def start():
    return render_template("fakeform.html")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224, debug=True)
  # app.run(host="0.0.0.0", port=2224, debug=True)
