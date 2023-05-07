from utiles import *


def r2():
    db = get_connection(False)
    print("Successfully connected to MySQL")
    # Créer le curseur qui permet de faire des queries et commandes SQL
    c = db.cursor()
    requete = """SELECT p.NomPath, p.NomSpec
                 FROM pathologie p
                 WHERE p.NomSpec IN 
                    (SELECT NomSpec 
                    FROM specsystanat 
                    GROUP BY NomSpec 
                    HAVING COUNT(DISTINCT NomSystAnat) = 1)"""
    c.execute(requete)
    result = ""
    i = 0
    for elem in c:
        i += 1
        result += str(i) + " | " + str(elem) + "<br>"
    return str(i) + " éléments ont été sélectionnés <br>" + result
