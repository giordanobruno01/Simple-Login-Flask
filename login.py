from flask import Flask, render_template, request, url_for
# Create a virtual enviroment : python3 -m venv .venv
# Activate enviroment :  . .venv/bin/activate
# Install Flask: pip3 install Flask
objLogin = Flask("login")
@objLogin.route("/", methods= ["POST", "GET"])
def loginUser():
   emailuser = request.form["emails"]
   password = request.form["password"]
   return (emailuser+" "+password)
#    return render_template("index.html")

objLogin.run(debug=True)