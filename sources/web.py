from flask import Flask, render_template, request  # pip install flask
from con_patient import *

app = Flask(__name__)

PATIENT = 2017845529
DCI = "IBUPROFENE"
DATE = "2019-01-01"
NOMCOMMERCIAL = "ACINAX"


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


@app.route("/get-string1", methods=["POST"])
def get_string1():
    import Requetes.r1 as r1

    global DCI
    DCI = request.form["DCI"]
    result = (
        "Requête 1: 'La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement'<br>"
        + "DCI: "
        + DCI
        + "<br>"
        + r1.execute_requete1(DCI)
    )
    return render_template("index.html", result=result)


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
        "Requête 4: 'Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) après une date donnée, par exemple en cas de rappel de produit pour lot contaminé (Acinax après 01/01/1980)'<br>"
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
        + execute_requete("./sources/Requetes/r6b.sql")
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


@app.route("/get-infomedpatient", methods=["GET"])
def get_infomedpatient():
    # TO DO : Récupérer les informations médicales du patient
    return "Informations du patients: " + str(PATIENT)


@app.route("/connexion-patient", methods=["POST"])
def connexion_patient():
    niss = request.form.get("NISSPatient")
    print("Niss récupéré:", niss)
    if niss is not None:
        global PATIENT
        PATIENT = niss
        msg2 = select_patient_info(niss)
        print(msg2)
    else:
        msg2 = "Patient non trouvé !"
    return render_template("index.html", msg2=msg2)


@app.route("/modif-inami", methods=["POST"])
def modif_inami():
    inami_phar = request.form.get("newinamiphar")
    inami_med = request.form.get("newinamimed")
    print(inami_phar, inami_med)
    msg = modif_inami_patient(PATIENT, inami_med, inami_phar)
    return render_template("index.html", msg=msg)


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
    msg = insert_patient(niss, inami_med, inami_pharma, mail, Bdate, nom, prenom, tel)
    return render_template(
        "index.html",
        message=msg,
    )


@app.route("/ajouter_medecin", methods=["POST"])
def ajouter_medecin():
    inami = request.form.get("inami_med")
    mail = request.form.get("mailmed")
    nom = request.form.get("nomMed")
    tel = request.form.get("telephoneMed")
    specialite = request.form.get("Specialite")
    print(inami, mail, nom, tel, specialite)
    msg = insert_medecin(inami, mail, nom, tel, specialite)
    return render_template("index.html", message=msg)


@app.route("/ajouter_pharmacien", methods=["POST"])
def ajouter_pharmacien():
    inami = request.form.get("inami_pharma")
    mail = request.form.get("mailpharma")
    nom = request.form.get("nomPharma")
    tel = request.form.get("telephonePharma")
    print(inami, mail, nom, tel)
    msg = insert_pharmacien(inami, mail, nom, tel)
    return render_template("index.html", message=msg)


if __name__ == "__main__":
    app.run(debug=True)
