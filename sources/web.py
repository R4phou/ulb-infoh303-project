from flask import Flask, render_template, request  # pip install flask

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
    import r1 as r1

    return r1.r1()


# Route pour récupérer la chaîne de caractères 2


@app.route("/get-string2", methods=["GET"])
def get_string2():
    import r2 as r2

    return r2.r2()


# Route pour récupérer la chaîne de caractères 3


@app.route("/get-string3", methods=["GET"])
def get_string3():
    import r3 as r3

    return r3.r3()


"""
POUR AJOUTER LES REQUETES SUIVANTES,
Creer un fichier r4.py dans le dossier sources
mettre la requete dans une fonction r4() (voir r1.py, r2.py, r3.py)
ajouter les lignes suivantes dans ce fichier en modifiant les chiffres par le num de la requete
"""

# @app.route("/get-string4", methods=["GET"])
# def get_string4():
#     import r4 as r4

#     return r4.r4()


@app.route("/get-string9", methods=["GET"])
def get_string9():
    import r9 as r9

    return r9.r9()


@app.route("/get-string10", methods=["GET"])
def get_string10():
    import r10 as r10

    return r10.r10()


if __name__ == "__main__":
    app.run(debug=True)
