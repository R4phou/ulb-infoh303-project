import mysql.connector

# Se connecter au serveur MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="ZQ$G7ZWr;b|rD]B",
    passwd="root",
)


print("Successfully connected to MySQL")

# Créer le curseur qui permet de faire des queries et commandes SQL
c = db.cursor()

# Supprimer la base de données si elle existe
c.execute("DROP DATABASE IF EXISTS systeme_medical")

# Créer la base de données
c.execute("CREATE DATABASE systeme_medical")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="ZQ$G7ZWr;b|rD]B",
    passwd="root",
    database="systeme_medical"
)

c = db.cursor()

query = """CREATE TABLE Patient 
    (NISS INT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Fname VARCHAR(50) NOT NULL,
    Bdate DATE NOT NULL,
    Email VARCHAR(50),
    Phone INT)"""
c.execute(query)
print("Table Patient created successfully")


query = """CREATE TABLE Medecin
    (
    INAMI INT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone INT,
    Speciality VARCHAR(50)
    )
"""
c.execute(query)
print("Table Medecin created successfully")


query = """CREATE TABLE Pharmacien
    (INAMI INT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone INT)
"""
c.execute(query)
print("Table Pharmacien created successfully")


query = """CREATE TABLE Medicament
    (
    NameMedicament VARCHAR(50) PRIMARY KEY,
    DCI VARCHAR(50) NOT NULL,
    Quantity INT NOT NULL)
"""
c.execute(query)
print("Table Medicament created successfully")


query = """CREATE TABLE AnatSystem
    (NameAnatSystem VARCHAR(50) PRIMARY KEY)
"""
c.execute(query)
print("Table AnatSystem created successfully")

query = """CREATE TABLE Pathologie
    (
    NamePathologie VARCHAR(50) PRIMARY KEY,
    FOREIGN KEY(NameAnatSystem) REFERENCES AnatSystem(NameAnatSystem))
"""
c.execute(query)
print("Table Pathologie created successfully")

# query = """CREATE TABLE Traitement
#     (
#     NameTrait VARCHAR(50) PRIMARY KEY,
#     DateBegin DATE NOT NULL,
#     Duration INT NOT NULL,
#     FOREIGN KEY (NISS) REFERENCES Patient(NISS))
# """
# c.execute(query)
# print("Table Traitement created successfully")


# query = """CREATE TABLE TraitementPathologie
#     (
#     FOREIGN KEY (NameTrait) REFERENCES Traitement(NameTrait),
#     FOREIGN KEY (NamePath) REFERENCES Pathologie(NamePathologie))
# """
# c.execute(query)
# print("Table TraitementPathologie created successfully")

# query = """CREATE TABLE Diagnostic
#     (FOREIGN KEY (NISS) REFERENCES Patient(NISS),
#     FOREIGN KEY (NomPathologie) REFERENCES Pathologie(NomPathologie),
#     FOREIGN KEY (NomTraitement) REFERENCES Traitement(NomPathologie),
#     DiagnosticDate DATE NOT NULL)
# """
# c.execute(query)
# print("Table Diagnostic created successfully")


# Fermeture de la connexion
db.commit()
c.close()
db.close()
