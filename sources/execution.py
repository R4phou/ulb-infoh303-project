from utiles import *
from Requetes.r2 import R2

#initiation de la connexion
db = get_connection(False)
cursor = db.cursor()

#Execution de la requete
cursor.execute(R2)

#Affichage du resultat
print(cursor.fetchall())