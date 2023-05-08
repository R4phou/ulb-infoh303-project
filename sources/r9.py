from utiles import *


def r9():
    """Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament."""
    db = get_connection(False)
    print("Successfully connected to MySQL")
    # Créer le curseur qui permet de faire des queries et commandes SQL
    c = db.cursor()
    requete = """SELECT p.LName, p.Fname, COUNT(DISTINCT dp.InamiMed)
                 FROM DossierPatient dp, Patient p
                 WHERE dp.NISSPatient = p.NISS
                 GROUP BY p.LName, p.Fname
                 
    """
    c.execute(requete)
    result = ""
    i = 0
    for elem in c:
        i += 1
        result += str(i) + " | " + str(elem) + "<br>"
    return str(i) + " éléments ont été sélectionnés <br>" + result


if __name__ == "__main__":
    print(r9())
