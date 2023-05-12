from utiles import *


db = get_connection(False)
cursor = db.cursor()


def select_patient_info(niss):
    cursor = db.cursor()
    try:
        cursor.execute(
            "SELECT INAMImed, INAMIPhar FROM patient WHERE niss = '" + str(niss) + "'"
        )
        result = "Bienvenue Patient " + str(niss) + "<br>"
        for element in cursor:
            result += "Médecin de référence: " + str(element[0]) + "<br>"
            result += "Pharmacien de référence: " + str(element[1])
    except:
        result = "Données du patient" + str(niss) + "non trouvées"
    return result


def insert_patient(niss, inami_med, inami_pharma, mail, Bdate, nom, prenom, tel):
    cursor = db.cursor()
    if tel == None:
        tel = ""
    if mail == None:
        mail = ""
    try:
        requete = (
            "INSERT INTO patient (NISS, Lname, Fname, Bdate, Email, Phone, INAMImed, INAMIphar) VALUES ("
            + str(niss)
            + " , "
            + str(nom)
            + ", "
            + str(prenom)
            + ", "
            + str(Bdate)
            + ", "
            + str(mail)
            + ", "
            + str(tel)
            + ", "
            + str(inami_med)
            + ", "
            + str(inami_pharma)
            + ")"
        )
        cursor.execute(requete)

        result = "Patient " + str(niss) + "ajouté avec succès"
    except:
        result = "Le patient n'a pas pu être ajouté à la base de données."
    return result


def insert_medecin(inami, mail, nom, tel, spec):
    cursor = db.cursor()
    if mail == None:
        mail = ""
    try:
        requete = (
            "INSERT INTO medecin (INAMI, Lname, Email, Phone, Speciality) VALUES ("
            + str(inami)
            + " , "
            + str(nom)
            + ", "
            + str(mail)
            + ", "
            + str(tel)
            + ", "
            + str(spec)
            + ")"
        )
        cursor.execute(requete)
        result = "Médecin " + str(inami) + "ajouté avec succès"
    except:
        result = "Le médecin n'a pas pu être ajouté à la base de données."
    return result


def insert_pharmacien(inami, mail, nom, tel):
    cursor = db.cursor()
    if mail == None:
        mail = ""
    try:
        requete = (
            "INSERT INTO pharmacien (INAMI, Lname, Email, Phone) VALUES ("
            + str(inami)
            + " , "
            + str(nom)
            + ", "
            + str(mail)
            + ", "
            + str(tel)
            + ")"
        )
        cursor.execute(requete)

        result = "Pharmacien " + str(inami) + "ajouté avec succès"
    except:
        result = "Le pharmacien n'a pas pu être ajouté à la base de données."
    return result


def modif_inami_patient(patient, inami_med, inami_phar):
    cursor = db.cursor()
    if inami_med != None:
        # INSERT MED
        var = 1
    if inami_phar != None:
        # INSERT PHAR
        var = 1
    result = "Le pharmacien n'a pas pu être ajouté à la base de données."
    return result
