from flask import Flask, render_template, request, url_for, redirect
# Create a virtual enviroment : python3 -m venv .venv
# Activate enviroment :  . .venv/bin/activate
# Install Flask: pip3 install Flask

app = Flask("login")
@app.route("/", methods= ["POST", "GET"])
def loginUser():
      if(request.method =="POST"):
            var1 = request.form["n1"]
            var2 = request.form["n2"]
            # reader = open("UserListDB.txt", "r")

            # v =reader.readline().strip()
            # log =0
            return render_template("results.html", res = str(request.method + " if"))
            # while(v!=""):
            #       l = v.split(" ")
            #       if(var1==l[0] and var2 ==l[1]):
            #             log =1
            #       v = reader.readline().strip()
            # if(log ==1):
            # return render_template("results.html", res = log+ " logged sucessfuly ") 
            # else:
            #       return render_template("results.html", res = "bad credentials")

      else:
            return render_template("results.html", res = str(request.method + " else"))
            


  

app.run(debug=True)