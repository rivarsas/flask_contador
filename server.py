from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "ELPEPE"


@app.route("/")
def root():

    if 'count' in session:
        print('la llave existe!')
        session["count"] += 1
    else:
        print("la llave 'count' NO existe")
        session["count"] = 0

    return render_template("index.html", count=session["count"])


@app.route("/add", methods=["POST"])
def add():
    if(request.form["incremento"]!=""):

        session["count"] += int(request.form["incremento"])-1

    print(request.form)
    return redirect("/")


@app.route("/destroy_session", methods=["POST"])
def reset():
    session.clear()	
    return redirect("/")


if(__name__ == "__main__"):
    app.run(debug=True)
