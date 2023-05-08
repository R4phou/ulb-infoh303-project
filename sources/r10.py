from utiles import *


def r10():
    """La liste de médicament n’étant plus prescrit depuis une date spécifique."""
    db = get_connection(False)
    print("Successfully connected to MySQL")
    # Créer le curseur qui permet de faire des queries et commandes SQL
    c = db.cursor()
    requete = """SELECT DISTINCT med.DCI, med.NomCom, med.systAnat
                 FROM Medicament med
                 WHERE med.NomCom in
                    (SELECT dp.NomComMedicament
                      FROM DossierPatient dp
                      WHERE dp.datePrescription < '1999-01-01')
    """
    c.execute(requete)
    result = ""
    i = 0
    for elem in c:
        i += 1
        result += str(i) + " | " + str(elem) + "<br>"
    return str(i) + " éléments ont été sélectionnés <br>" + result
