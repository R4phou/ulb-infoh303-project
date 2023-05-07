from utiles import *


def r1():
    db = get_connection(False)
    print("Successfully connected to MySQL")
    # Créer le curseur qui permet de faire des queries et commandes SQL
    c = db.cursor()
    requete = """SELECT * FROM pathologie"""
    c.execute(requete)
    result = ""
    i = 0
    for elem in c:
        i += 1
        result += str(i) + " | " + str(elem) + "<br>"
    return str(i) + " éléments ont été sélectionnés <br>" + result
