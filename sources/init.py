from utiles import *

#Noms des tables de la base de données "systeme_medical"
TABLE_NAMES = ["Patient","Medecin","Pharmacien","Medicament","AnatSystem","Pathologie","Traitement","TraitementPathologie","Diagnostic"]

#Connexion au serveur MySQL
db = get_connection(False)
cursor = db.cursor()

#Tronque l'entièreté de la table
def reset_table_data(table):
    query = "DELETE FROM " + table
    execute_query(cursor,query)

#Tronque l'entièreté de la base de données
def reset_all_tables():
    for table in TABLE_NAMES:
        reset_table_data(table)

#Insère des données (sous forme de string) dans une table
def insert_data(table,parameters,values):
    query = "INSERT INTO " + table +str(""+str(tuple(parameters)).replace("'",'')) +" VALUES (" + values_to_str(list(values))+");"
    print(query)
    execute_query(cursor,query)

#Ajoute les données de Patient.xml dans la table Patient
def copy_patients_to_db():
    root = load_xml_file("Données/patient.xml")
    for data in root:
        patient = get_data_as_dictionary(data)
        #Réordonne les données selon le mapping de la table Patient
        values = {PATIENT_NODE_MAPPING[k]:patient[k] for k in PATIENT_NODE_MAPPING.keys() if k in patient and patient[k] != 'NULL'}
        birth_date = values['Bdate']
        values['Bdate'] = format_to_date(birth_date)
        insert_data("Patient",values.keys(),values.values())

if __name__ == "__main__":
    reset_all_tables()
    copy_patients_to_db()
    close_db(db,cursor)