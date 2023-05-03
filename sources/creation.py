from utiles import *
from Requetes.create_tables import get_table_creation_queries

# Se connecter au serveur MySQL
db = get_connection(True)

print("Successfully connected to MySQL")

# Créer le curseur qui permet de faire des queries et commandes SQL
c = db.cursor()

# Supprimer la base de données si elle existe
execute_query(c, "DROP DATABASE IF EXISTS systeme_medical")

# Créer la base de données
execute_query(c, "CREATE DATABASE systeme_medical")

# Connection à la base de données "systeme_medical"
db = get_connection(False)
c = db.cursor()

# Création des tables
queries = get_table_creation_queries()
execute_queries(c, queries)
print("Successfully created tables")

# Fermeture de la connexion
close_db(db, c)
