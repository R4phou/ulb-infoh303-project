from utiles import *

#initiation de la connexion
db = get_connection(False)
cursor = db.cursor()

#Requete 2
R2 = """SELECT p.NomPath, p.NomSpec
FROM systeme_medical.pathologie p
WHERE p.NomSpec IN 
    (SELECT NomSpec 
     FROM systeme_medical.specsystanat 
     GROUP BY NomSpec 
     HAVING COUNT(DISTINCT NomSystAnat) = 1);
"""

#Execution de la requete
cursor.execute(R2)

#Affichage du resultat
print(cursor.fetchall())