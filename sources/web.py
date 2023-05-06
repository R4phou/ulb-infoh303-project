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
    return string1


# Route pour récupérer la chaîne de caractères 2


@app.route("/get-string2", methods=["GET"])
def get_string2():
    return string2


# Route pour récupérer la chaîne de caractères 3


@app.route("/get-string3", methods=["GET"])
def get_string3():
    return string3


if __name__ == "__main__":
    app.run(debug=True)
