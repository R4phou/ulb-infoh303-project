from utiles import *


db = get_connection(False)


def check_patient(niss):
    cursor = db.cursor()
    print(niss)
    if niss == None:
        return False
    try:
        cursor.execute("SELECT niss FROM patient WHERE niss = '" + str(niss) + "'")
        cursor.close()
        return True
    except:
        return False


def select_patient_info(niss):
    try:
        cursor = db.cursor()
        query = "SELECT INAMImed, INAMIPhar FROM patient WHERE NISS = " + str(niss)
        cursor.execute(query)
        result = "Bienvenue Patient " + str(niss) + "<br>"
        for element in cursor:
            result += "Médecin de référence: " + str(element[0]) + "<br>"
            result += "Pharmacien de référence: " + str(element[1])
        cursor.close()
    except:
        result = "Données du patient " + str(niss) + " non trouvées"
    return result


def insert_patient(niss, inami_med, inami_pharma, mail, Bdate, nom, prenom, tel):
    if tel == None:
        tel = ""
    if mail == None:
        mail = ""
    try:
        cursor = db.cursor()
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
        cursor.close()
        result = "Patient " + str(niss) + "ajouté avec succès"
    except:
        result = "Le patient n'a pas pu être ajouté à la base de données."
    return result


def insert_medecin(inami, mail, nom, tel, spec):
    if mail == None:
        mail = ""
    try:
        cursor = db.cursor()
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
        cursor.close()
        result = "Médecin " + str(inami) + "ajouté avec succès"
    except:
        result = "Le médecin n'a pas pu être ajouté à la base de données."
    return result


def insert_pharmacien(inami, mail, nom, tel):
    if mail == None:
        mail = ""
    try:
        cursor = db.cursor()
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
        cursor.close()
        result = "Pharmacien " + str(inami) + "ajouté avec succès"
    except:
        result = "Le pharmacien n'a pas pu être ajouté à la base de données."
    return result


def modif_inami_patient(patient, inami_med, inami_phar):
    result = "Aucun médecin ou pharmacien n'a été ajouté."
    if inami_med != None:
        try:
            cursor = db.cursor()
            query = (
                "UPDATE patient SET INAMImed = '"
                + str(inami_med)
                + "' WHERE NISS = '"
                + str(patient)
                + "'"
            )
            print(query)
            cursor.execute(query)
            result = (
                "Médecin de référence modifié avec succès <br> Votre nouveau médecin de référence est: "
                + str(inami_med)
                + "<br>"
            )
            cursor.close()
        except:
            result = "Rien n'a pas pu être ajouté à la base de données."
    if inami_phar != None:
        try:
            cursor = db.cursor()
            query = (
                "UPDATE patient SET INAMIphar = '"
                + str(inami_phar)
                + "' WHERE NISS = '"
                + str(patient)
                + "'"
            )
            print(query)
            cursor.execute(query)
            result = (
                "Médecin de référence modifié avec succès <br> Votre nouveau médecin de référence est: "
                + str(inami_phar)
                + "<br>"
            )
            cursor.close()
        except:
            result = "Rien n'a pas pu être ajouté à la base de données."
    return result


if __name__ == "__main__":
    print(select_patient_info(2017845529))
