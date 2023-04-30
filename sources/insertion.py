import mysql.connector
import xml.etree.ElementTree as ET
from utiles import *

db = get_connection(False)

c = db.cursor()

# Chemin vers le fichier XML
xml_file_path = "Données/patient.xml"

# Analyse du fichier XML et stockage des données dans une liste
tree = ET.parse(xml_file_path)
root = tree.getroot()

patients = []
for patient in root.findall('personne'):
    NISS = patient.find('NISS').text
    Lname = patient.find('nom').text
    Fname = patient.find('prenom').text
    Bdate = patient.find('date_de_naissance').text
    Email = patient.find('mail').text
    Phone = patient.find('telephone').text
    patients.append((NISS,Lname,Fname,Bdate,Email,Phone))

# Insertion des données dans la table "patients" de la base de données
for patient in patients:
    c.execute("INSERT INTO Patient (NISS, Lname, Fname, Bdate, Email, Phone) VALUES (%s, %s, %s, %s, %s)", patient)

c.execute("SELECT * FROM Patient")
print(c.fetchall())

# Fermeture de la connexion
close_db(db,c)
