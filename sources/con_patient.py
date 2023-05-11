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
