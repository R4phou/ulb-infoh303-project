from utiles import *
from mappings import *

# Noms des tables de la base de données "systeme_medical"
TABLE_NAMES = [
    "SpecSystAnat",
    "Medecin",
    "Pharmacien",
    "Patient",
    "Medicament",
    "Pathologie",
    "Diagnostic",
    "DossierPatient",
]

# Connexion au serveur MySQL
db = get_connection(False)
cursor = db.cursor()

# Tronque l'entièreté de la table


def reset_table_data(table):
    query = "DELETE FROM " + table
    execute_query(cursor, query)


# Tronque l'entièreté de la base de données


def reset_all_tables():
    for table in reversed(TABLE_NAMES):
        reset_table_data(table)


# Insère des données (sous forme de string) dans une table


def insert_data(table, parameters, values):
    query = (
        "INSERT INTO "
        + table
        + str("" + str(tuple(parameters)).replace("'", ""))
        + " VALUES ("
        + values_to_str(list(values))
        + ");"
    )
    execute_query(cursor, query)


def line_to_data(mapping, dico):
    return {
        mapping[k]: dico[k] for k in mapping.keys() if k in dico and dico[k] != "NULL"
    }


def insert_xml(path, mapping, name):
    print("Inserting " + name + " ...")
    root = load_xml_file(path)
    for data in root:
        item = get_data_as_dictionary(data)
        # item: {key : [a,b,c]}
        lines = flatMapping(item)
        for data in lines:
            l = []
            values = line_to_data(mapping, data)
            if name == "Patient":
                birth_date = values["Bdate"]
                values["Bdate"] = format_to_date(birth_date)
            if name == "Diagnostic":
                birth_date = values["BirthDate"]
                values["BirthDate"] = format_to_date(birth_date)
                diag_date = values["date"]
                values["date"] = format_to_date(diag_date)
            if values not in l:
                l.append(values)
            insert_list(l, name)
    print("Table " + name + " inserted")
    db.commit()


def insert_csv(path, mapping, name, columns, skip=0):
    print("Inserting " + name + " ...")
    mat = load_csv_file(path, skip)
    l = []
    for data in range(skip, len(mat)):
        item = get_data_as_dictionary_csv(mat[data], columns)
        values = line_to_data(mapping, item)
        if values not in l:
            l.append(values)
        if name == "DossierPatient":
            datepre = values["datePrescription"]
            values["datePrescription"] = format_to_date(datepre)
            dateven = values["dateVente"]
            values["dateVente"] = format_to_date(dateven)
    insert_list(l, name)
    print("Table " + name + " inserted")
    db.commit()


def insert_list(list, name):
    for item in list:
        insert_data(name, item.keys(), item.values())


def init_db():
    reset_all_tables()
    print("Tables reset")
    insert_xml("Données/specialites.xml", SPECIALITE_NODE_MAPPING, "SpecSystAnat")
    insert_xml("Données/medecins.xml", MEDECIN_NODE_MAPPING, "Medecin")
    insert_xml("Données/pharmaciens.xml", PHARMACIEN_NODE_MAPPING, "Pharmacien")
    insert_csv(
        "Données/medicaments.csv",
        MEDICAMENT_NODE_MAPPING,
        "Medicament",
        ["dci", "nom Commercial", "système anatomique", "conditionnement"],
        1,
    )
    insert_xml("Données/patient.xml", PATIENT_NODE_MAPPING, "Patient")
    insert_csv(
        "Données/pathologies.csv",
        PATHOLOGIE_NODE_MAPPING,
        "Pathologie",
        ["name", "specialite"],
        0,
    )
    insert_xml("Données/diagnostiques.xml", DIAGNOSTIC_NODE_MAPPING, "Diagnostic")
    insert_csv(
        "Données/dossiers_patients.csv",
        DOSSIER_NODE_MAPPING,
        "DossierPatient",
        [
            "NISS_patient",
            "medecin",
            "inami_medecin",
            "pharmacien",
            "inami_pharmacien",
            "medicament_nom_commercial",
            "DCI",
            "date_prescription",
            "date_vente",
            "duree_traitement",
        ],
        1,
    )
    close_db(db, cursor)
    return "La base de données a été correctement initialisée!"


if __name__ == "__main__":
    print(init_db())
