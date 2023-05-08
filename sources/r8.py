from utiles import *


def r8():
    """Quelle est la pathologie la plus diagnostiquée ?"""
    db = get_connection(False)
    print("Successfully connected to MySQL")
    # Créer le curseur qui permet de faire des queries et commandes SQL
    c = db.cursor()
    requete = """ SELECT path.NomPath
                  FROM pathologie path
                  JOIN diagnostic diag ON path.NomPath = diag.NomPathologie
                  GROUP BY path.NomPath
                  HAVING COUNT(*) >= ALL (
                      SELECT COUNT(*)
                      FROM diagnostic diag2
                      WHERE diag2.NomPathologie <> path.NomPath
                      GROUP BY diag2.NomPathologie
                  )
    """
    c.execute(requete)
    result = ""
    i = 0
    for elem in c:
        i += 1
        result += str(i) + " | " + str(elem) + "<br>"
    return str(i) + " éléments ont été sélectionnés <br>" + result


if __name__ == "__main__":
    print(r8())
