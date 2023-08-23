from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user,LoginManager

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
      if(request.method =="POST"):
            username = request.form.get("signName")
            email = request.form.get("signEmail")
            passwords = request.form.get("signPassword")
            if not username and not email and not passwords:

                  email = request.form.get("loginEmail")
                  passwords = request.form.get("loginPassword")

                  conn = get_db_connection()
                  user = conn.execute('SELECT * FROM users WHERE email = ? AND passwords = ?', (email, passwords)).fetchone() 
                  conn.close()
                  if user is None: 
                  
                        return render_template("input.html" , message = "User does not Exists")
                        # abort(404)
                  return redirect(url_for("shopMethod", name =user["username"]) )
            else: 

                  connectio = get_db_connection()
                  user = connectio.execute('SELECT * FROM users WHERE email = ? AND passwords = ?', (email, passwords)).fetchone() 
                  # connectio.close()
                  if user is None:  
            
                        users = connectio.execute('INSERT INTO users (username, email, passwords) VALUES (?, ?,?)', (username, email, passwords))
                        connectio.commit()
                        connectio.close()
                  
                        # flash("User Created", 'your bootstrap category[eg:success, primary, etc]')
                        return render_template("input.html" , message = "User Created" )
                  else:
                         
                        return render_template("input.html", message = "User Already Exists" )

      else:
            return render_template("input.html" )
            abort(404)

@app.route("/shop/<name>", methods = ["GET", "POST"])

def shopMethod(name):
      if(request.method == "POST"):
            chocolate = int(request.form.get("chocolate"))
            soda = int(request.form.get("soda"))
            banana = int(request.form.get("banana"))
            pizza = int(request.form.get("pizza"))

            total = chocolate + soda + banana + pizza

            return render_template("checkout.html", res = total,cust = name, chocoQ = chocolate, sodaQ = soda//2, bananaQ = banana//3, pizzaQ = pizza//4)
      else:
            return render_template("shop.html")
# @app.route("/<username>")
# def lgi(username):
#       return render_template("results.html", res = username + " logged with url " )


app.run(debug=True)