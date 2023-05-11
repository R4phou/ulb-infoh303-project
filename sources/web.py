from flask import Flask, render_template, request  # pip install flask
from con_patient import *

app = Flask(__name__)

# Définition des chaînes de caractères à afficher
string1 = "Bonjour!"
string2 = "Comment ça va ?"
string3 = "Quelle heure est-il ?"

PATIENT = 2017845529


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


@app.route("/get-string1", methods=["GET"])
def get_string1():
    return (
        "Requête 1: 'La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement'<br>"
        + execute_requete("./sources/Requetes/r1.sql")
    )


@app.route("/get-string2", methods=["GET"])
def get_string2():
    return (
        "Requête 2: 'La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes'<br>"
        + execute_requete("./sources/Requetes/r2.sql")
    )


@app.route("/get-string3", methods=["GET"])
def get_string3():
    return (
        "Requête 3: 'La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments'<br>"
        + execute_requete("./sources/Requetes/r3.sql")
    )


@app.route("/get-string4", methods=["GET"])
def get_string4():
    return (
        "Requête 4: 'Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) après une date donnée, par exemple en cas de rappel de produit pour lot contaminé'<br>"
        + execute_requete("./sources/Requetes/r4.sql")
    )


@app.route("/get-string5", methods=["GET"])
def get_string5():
    return (
        "Requête 5: 'Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patient suive bien un traitement chronique'<br>"
        + execute_requete("./sources/Requetes/r5.sql")
    )


@app.route("/get-string6", methods=["GET"])
def get_string6():
    return (
        "Requête 6: 'La liste des médecins ayant prescrit des médicaments ne relevant pas de leur spécialité'<br>"
        + execute_requete("./sources/Requetes/r6.sql")
    )


@app.route("/get-string7", methods=["GET"])
def get_string7():
    return (
        "Requête 7: 'Pour chaque décennie entre 1950 et 2020, (1950 − 59, 1960 − 69, ...), le médicament le plus consommé par des patients nés durant cette décennie'<br>"
        + execute_requete("./sources/Requetes/r7.sql")
    )


@app.route("/get-string8", methods=["GET"])
def get_string8():
    return (
        "Requête 8: 'Quelle est la pathologie la plus diagnostiquée ?'<br>"
        + execute_requete("./sources/Requetes/r8.sql")
    )


@app.route("/get-string9", methods=["GET"])
def get_string9():
    return (
        "Requête 9: 'Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament'<br>"
        + execute_requete("./sources/Requetes/r9.sql")
    )


@app.route("/get-string10", methods=["GET"])
def get_string10():
    return (
        "Requête 10: 'La liste de médicament n’étant plus prescrit depuis une date spécifique' <br>"
        + execute_requete("./sources/Requetes/r10.sql")
    )


@app.route("/getinfo", methods=["GET"])
def get_info():
    return select_patient_info(PATIENT)


@app.route("/get-infomedpatient", methods=["GET"])
def get_infomedpatient():
    # TO DO : Récupérer les informations médicales du patient
    return "Informations du patients: " + str(PATIENT)


@app.route("/", methods=["POST"])
def reset():
    val = request.form.get("Reset")
    if val == "True":
        return render_template("/")
    else:
        return render_template("/index.html")


@app.route("/connexion-patient", methods=["POST"])
def connexion_patient():
    niss = request.form.get("NISSPatient")
    if niss != None:
        global PATIENT
        PATIENT = niss
        # TO DO RECUPERER LE MEDECIN ET PHARMACIEN DE REFERENCE DU PATIENT
    return render_template("index.html")


@app.route("/ajouter_patient", methods=["POST"])
def ajouter_patient():
    niss = request.form.get("NISS")
    mail = request.form.get("mail")
    Bdate = request.form.get("date_de_naissance")
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    inami_med = request.form.get("inami_medecin")
    inami_pharma = request.form.get("inami_pharmacien")
    tel = request.form.get("telephone")
    print(niss, mail, Bdate, nom, prenom, inami_med, inami_pharma, tel)
    return render_template(
        "index.html",
        message="Le patient a été ajouté dans la base de données avec succès!",
    )


@app.route("/ajouter_medecin", methods=["POST"])
def ajouter_medecin():
    inami = request.form.get("inami_med")
    mail = request.form.get("mailmed")
    nom = request.form.get("nomMed")
    tel = request.form.get("telephoneMed")
    specialite = request.form.get("Specialite")
    print(inami, mail, nom, tel, specialite)
    message = "Le médecin a été ajouté dans la base de données avec succès!"  # Message qui va être écrit dans le paragraphe en dessous (dire si erreur!)
    return render_template("index.html", message=message)


@app.route("/ajouter_pharmacien", methods=["POST"])
def ajouter_pharmacien():
    inami = request.form.get("inami_pharma")
    mail = request.form.get("mailpharma")
    nom = request.form.get("nomPharma")
    tel = request.form.get("telephonePharma")
    print(inami, mail, nom, tel)
    message = "Le pharmacien a été ajouté dans la base de données avec succès!"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
