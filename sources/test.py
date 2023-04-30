from utiles import *
import re

data = '''
  <patient>
    <NISS>184232301592</NISS>
    <date_de_naissance>03/28/1924</date_de_naissance>
    <genre>2</genre>
    <inami_medecin>158848164732</inami_medecin>
    <inami_pharmacien> 94709786082</inami_pharmacien>
    <mail></mail>
    <nom>HAMEL</nom>
    <prenom>Audelia</prenom>
    <telephone></telephone>
  </patient>


  <patient>
    <NISS>477186174799</NISS>
    <date_de_naissance>12/04/1981</date_de_naissance>
    <genre>5</genre>
    <inami_medecin>298243888847</inami_medecin>
    <inami_pharmacien>319636766184</inami_pharmacien>
    <mail>E.GUILBERT@hotmail.com</mail>
    <nom>GUILBERT</nom>
    <prenom>Ellande</prenom>
    <telephone>+32862967279731</telephone>
  </patient>

'''

with open("Données/patient.xml") as f:
    xml_f = f.read()
    formated = "<root>" + data + "</root>"
    root = etree.fromstring(formated)
    for patient in root:
        for attribute in patient:
            print(attribute.tag, attribute.text)
        print("\n")


def insert_patient_query(NISS,LName,FName,Bdate,Email,Phone,INAMImed,INAMIphar):
    patient = [NISS,LName,FName,Bdate,Email,Phone,INAMImed,INAMIphar]
    return insert_patient_query(patient)