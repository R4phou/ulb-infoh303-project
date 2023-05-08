from flask import Flask, render_template, request  # pip install flask
from utiles import *

app = Flask(__name__)

# Définition des chaînes de caractères à afficher
string1 = "Bonjour!"
string2 = "Comment ça va ?"
string3 = "Quelle heure est-il ?"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/creer", methods=["GET"])
def creer():
    import creation as c

    return c.creation()


@app.route("/init", methods=["GET"])
def init():
    import init as i

    return i.init_db()


# Route pour récupérer la chaîne de caractères 1


@app.route("/get-string1", methods=["GET"])
def get_string1():
    return execute_requete("./Requetes/r1.sql")


@app.route("/get-string2", methods=["GET"])
def get_string2():
    return execute_requete("./Requetes/r2.sql")


@app.route("/get-string3", methods=["GET"])
def get_string3():
    return execute_requete("./Requetes/r3.sql")


@app.route("/get-string4", methods=["GET"])
def get_string4():
    return execute_requete("./Requetes/r4.sql")


@app.route("/get-string5", methods=["GET"])
def get_string5():
    return execute_requete("./Requetes/r5.sql")


@app.route("/get-string6", methods=["GET"])
def get_string6():
    return execute_requete("./Requetes/r6.sql")


@app.route("/get-string7", methods=["GET"])
def get_string7():
    return execute_requete("./Requetes/r7.sql")


@app.route("/get-string8", methods=["GET"])
def get_string8():
    return execute_requete("./Requetes/r8.sql")


@app.route("/get-string9", methods=["GET"])
def get_string9():
    return execute_requete("./Requetes/r9.sql")


@app.route("/get-string10", methods=["GET"])
def get_string10():
    return execute_requete("./Requetes/r10.sql")


if __name__ == "__main__":
    app.run(debug=True)
