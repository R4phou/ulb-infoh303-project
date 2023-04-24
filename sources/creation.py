import mysql.connector

# Se connecter au serveur MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="ZQ$G7ZWr;b|rD]B",
    passwd="root",
    database="testdb"
)


print("Successfully connected to MySQL database 'testdb'")

# Créer le curseur qui permet de faire des queries et commandes SQL
mycursor = db.cursor()

# Créer une base de données (à ne faire qu'une fois la première fois qu'on run le code)

# mycursor.execute("CREATE DATABASE testdb")
# print("Successfully created database 'testdb'")


"""Basic queries and commands"""


# Création d'une table avec 3 colonnes (name, age, personID)
# mycursor.execute(
#     "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# AUTO_INCREMENT permet d'incrémenter automatiquement la valeur de la colonne personID (éviter d'avoir 2 fois la même)


# Ajout d'informations dans la table Person
mycursor.execute(
    "INSERT INTO Person (name, age) VALUES (%s, %s)", ("Tim", 91))
db.commit()  # Commit les changements dans la base de données


# Visualiser les données de la table Person
mycursor.execute("SELECT * FROM Person")


# mycursor.execute("DESCRIBE Person")
for x in mycursor:
    print(x)
