from utiles import *


db = get_connection(False)
cursor = db.cursor()
db.autocommit=True #permet faire des commits auto lorsqu'une modif est apportée à la database 

def check_patient(niss):
    print(niss)
    if niss == None:
        return False
    try:
        cursor.execute("SELECT niss FROM patient WHERE niss = '" + str(niss) + "'")
        return True
    except:
        return False


def select_patient_info(niss):
    try:
        query = "SELECT INAMImed, INAMIPhar FROM patient WHERE NISS = " + str(niss)
        cursor.execute(query)
        result = "Bienvenue Patient " + str(niss) + "\n"
        for element in cursor:
            result += "Médecin de référence: " + str(element[0]) + "\n"
            result += "Pharmacien de référence: " + str(element[1])
    except:
        result = "Données du patient " + str(niss) + " non trouvées"
    return result


def insert_patient(niss, inami_med, inami_pharma, mail, Bdate, nom, prenom, tel):
    if tel == None:
        tel = ""
    if mail == None:
        mail = ""
    try:
        requete = (
            "INSERT INTO patient (NISS, Lname, Fname, Bdate, Email, Phone, INAMImed, INAMIphar) VALUES ("
            + str(niss)
            + " ,'"
            + str(nom)
            + "', '"
            + str(prenom)
            + "','"
            + str(Bdate)
            + "','"
            + str(mail)
            + "', "
            + str(tel)
            + ", "
            + str(inami_med)
            + ", "
            + str(inami_pharma)
            + ")"
        )
        cursor.execute(requete)
        result = "Patient " + str(niss) + " ajouté avec succès"
    except:
        result = "Le patient n'a pas pu être ajouté à la base de données."
    return result


def insert_medecin(inami, mail, nom, tel, spec):
    if mail == None:
        mail = ""
    try:
        requete = (
            "INSERT INTO medecin (INAMI, Lname, Email, Phone, Speciality) VALUES ("
            + str(inami)
            + ",'"
            + str(nom)
            + "','"
            + str(mail)
            + "',"
            + str(tel)
            + ",'"
            + str(spec)
            + "')"
        )
        print(requete)
        cursor.execute(requete)
        result = "Médecin " + str(inami) + " ajouté avec succès"
    except:
        result = "Le médecin n'a pas pu être ajouté à la base de données."
    return result


def insert_pharmacien(inami, mail, nom, tel):
    if mail == None:
        mail = ""
    try:
        requete = (
            "INSERT INTO pharmacien (INAMI, Lname, Email, Phone) VALUES ("
            + str(inami)
            + ",'"
            + str(nom)
            + "','"
            + str(mail)
            + "',"
            + str(tel)
            + ")"
        )
        cursor.execute(requete)
        result = "Pharmacien " + str(inami) + " ajouté avec succès"
    except:
        result = "Le pharmacien n'a pas pu être ajouté à la base de données."
    return result


def modif_inami_patient(patient, inami_med, inami_phar):
    result = "Bienvenue Patient " + str(patient) + "\n"
    if inami_med != None:
        try:
            query = (
                "UPDATE patient SET INAMImed = '"
                + str(inami_med)
                + "' WHERE NISS = '"
                + str(patient)
                + "'"
            )
            print(query)
            cursor.execute(query)
            result += (
                "Médecin de référence modifié avec succès \nVotre nouveau médecin de référence est: "
                + str(inami_med)
                + "\n"
            )
        except:
            result += "Le médecin n'a pas pu être modifié dans la base de données. \n"
    if inami_phar != None:
        try:
            query = (
                "UPDATE patient SET INAMIphar = '"
                + str(inami_phar)
                + "' WHERE NISS = '"
                + str(patient)
                + "'"
            )
            print(query)
            cursor.execute(query)
            result += (
                "Pharmacien de référence modifié avec succès \nVotre nouveau pharmacien de référence est: "
                + str(inami_phar)
                + "\n"
            )
        except:
            result += "Le pharmacien n'a pas pu être modifié à la base de données.\n"
    return result


if __name__ == "__main__":
    print(select_patient_info(2017845529))
