from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
import sqlite3

# ngrok http http://127.0.0.1:5000
# Create a virtual enviroment : python3 -m venv .venv
# Activate enviroment :  . .venv/bin/activate
# Install Flask: pip3 install Flask

app = Flask("login")#creating the flask obj (application) with the .py
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app.config['SECRET_KEY'] = 'giordano12345'
@app.route("/", methods= ["POST", "GET"])#route is the page/link opened on browser, post/get protocol which brower and python will comunicate (sent and receive data)

def createAccount():

      username = request.form["sigName"]
      email = request.form["signEmail"]
      password = request.form["signPassword"]
      if not username and not email and not password:
            loginUser()
      else:
            connectio = get_db_connection()
            users = connectio.execute('INSERT INTO posts (username, email, password) VALUES (?, ?,?)', (username, email, password))
            connectio.commit()
            connectio.close()
            connectio.close()
            if users is None:
                  abort(404)

            flash("user created")


def loginUser():

      if(request.method =="POST"):
            email = request.form["loginEmail"]
            password = request.form["loginPassword"]

            
            # while(v!=""):
            #       l = v.split(" ")
            #       if(var1==l[0] and var2 ==l[1]):
            #             # return redirect(url_for("loggedMethod", username = users[0]["email"]))
            #             return render_template("results.html", username = users[0]["email"])
                  
            #       v = reader.readline().strip()
            # # flash('Title is required!')      
            # return render_template("input.html", inv = "try again")
      else:
            return render_template("input.html", res =request.method)
            
# @app.route("/logged/<username>")
# def loggedMethod(username): 
#       return render_template("results.html", res = username + " logged " )

# @app.route("/<username>")
# def lgi(username):
#       return render_template("results.html", res = username + " logged with url " )


app.run(debug=True)