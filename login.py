from flask import Flask, render_template, request, url_for, redirect
import sqlite3
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create a virtual enviroment : python3 -m venv .venv
# Activate enviroment :  . .venv/bin/activate
# Install Flask: pip3 install Flask

app = Flask("login")

@app.route("/", methods= ["POST", "GET"])
def loginUser():
      conn = get_db_connection()
      users = conn.execute('SELECT * FROM users').fetchall()
      conn.close()

      if(request.method =="POST"):
            var1 = request.form["n1"]
            var2 = request.form["n2"]
            reader = open("UserListDB.txt", "r")

            v =reader.readline().strip()
            
            while(v!=""):
                  l = v.split(" ")
                  if(var1==l[0] and var2 ==l[1]):
                        # return redirect(url_for("loggedMethod", username = users[0]["email"]))
                        return render_template("results.html", username = users[0]["email"])
                  
                  v = reader.readline().strip()
                  
            return render_template("input.html", inv = "try again")
      else:
            return render_template("input.html", res =request.method)
            
@app.route("/logged/<username>")
def loggedMethod(username):
      return render_template("results.html", res = username + " logged " )

# @app.route("/<username>")
# def lgi(username):
#       return render_template("results.html", res = username + " logged with url " )


app.run(debug=True)