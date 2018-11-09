# coding: utf-8
from flask import Flask, render_template, request,redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",name="dak vad")

@app.route("/secure")
def secure():
    return render_template("graph.html")

@app.route("/", methods=["POST"])
def indexRet():
    login = request.form['login']
    mdp = request.form['mdp']
    error = ""
    if login!="admin" and mdp!="mdp":
        error="mauvaise donnees"
    else:
        return redirect(url_for('secure'))

    return render_template("index.html",error=error)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)