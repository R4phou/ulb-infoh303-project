from utiles import *
from mappings import *

# Noms des tables de la base de données "systeme_medical"
TABLE_NAMES = [
    "Patient",
    "Medecin",
    "Pharmacien",
    "Medicament",
    "SpecSystAnat",
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
    for table in TABLE_NAMES:
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
    # print(query)
    execute_query(cursor, query)


# Ajoute les données de Patient.xml dans la table Patient
def copy_patients_to_db():
    root = load_xml_file("Données/patient.xml")
    for data in root:
        patient = get_data_as_dictionary(data)
        # print(patient)
        # Réordonne les données selon le mapping de la table Patient
        values = {
            PATIENT_NODE_MAPPING[k]: patient[k]
            for k in PATIENT_NODE_MAPPING.keys()
            if k in patient and patient[k] != "NULL"
        }
        birth_date = values["Bdate"]
        values["Bdate"] = format_to_date(birth_date)
        insert_data("Patient", values.keys(), values.values())


# Ajoute les données de medecins.xml dans la table Patient


def copy_medecins_to_db():
    root = load_xml_file("Données/medecins.xml")
    for data in root:
        medecin = get_data_as_dictionary(data)
        # Réordonne les données selon le mapping de la table Patient
        values = {
            MEDECIN_NODE_MAPPING[k]: medecin[k]
            for k in MEDECIN_NODE_MAPPING.keys()
            if k in medecin and medecin[k] != "NULL"
        }
        insert_data("Medecin", values.keys(), values.values())


# Ajoute les données de pharmaciens.xml dans la table Patient


def copy_pharmaciens_to_db():
    root = load_xml_file("Données/pharmaciens.xml")
    for data in root:
        pharmacien = get_data_as_dictionary(data)
        # Réordonne les données selon le mapping de la table Patient
        values = {
            PHARMACIEN_NODE_MAPPING[k]: pharmacien[k]
            for k in PHARMACIEN_NODE_MAPPING.keys()
            if k in pharmacien and pharmacien[k] != "NULL"
        }
        insert_data("Pharmacien", values.keys(), values.values())


# Ajoute les données de pharmaciens.xml dans la table Patient


def copy_diagnostiques_to_db():
    root = load_xml_file("Données/diagnostiques.xml")
    for data in root:
        pharmacien = get_data_as_dictionary(data)
        # Réordonne les données selon le mapping de la table Patient
        values = {
            DIAGNOSTIC_NODE_MAPPING[k]: pharmacien[k]
            for k in DIAGNOSTIC_NODE_MAPPING.keys()
            if k in pharmacien and pharmacien[k] != "NULL"
        }
        birth_date = values["BirthDate"]
        values["BirthDate"] = format_to_date(birth_date)
        diag_date = values["date"]
        values["date"] = format_to_date(diag_date)
        insert_data("Diagnostic", values.keys(), values.values())


def copy_spec_to_db():
    root = load_xml_file("Données/specialites.xml")
    for data in root:
        specialite = get_data_as_dictionary(data)
        values = line_to_data(SPECIALITE_NODE_MAPPING, specialite)
        insert_data("SpecSystAnat", values.keys(), values.values())


def copy_medicament_to_db():
    mat = load_csv_file("Données/medicaments.csv")
    columns = mat[0]
    for i in range(1, len(mat)):
        medicament = get_data_as_dictionary_csv(mat[i], columns)
        values = line_to_data(MEDICAMENT_NODE_MAPPING, medicament)
        insert_data("Medicament", values.keys(), values.values())


def copy_pathologie_to_db():
    mat = load_csv_file("Données/pathologies.csv")
    columns = ["name", "specialite"]
    for i in range(0, len(mat)):
        pathologie = get_data_as_dictionary_csv(mat[i], columns)
        values = line_to_data(PATHOLOGIE_NODE_MAPPING, pathologie)
        insert_data("Pathologie", values.keys(), values.values())
        print("data inserted")


def line_to_data(mapping, dico):
    return {
        mapping[k]: dico[k] for k in mapping.keys() if k in dico and dico[k] != "NULL"
    }


def insert_xml(path, mapping, name):
    root = load_xml_file(path)
    l = []
    for data in root:
        item = get_data_as_dictionary(data)
        values = line_to_data(mapping, item)
        if values not in l:
            l.append(values)
    insert_list(l, name)


def insert_csv(path, mapping, name, columns, skip=0):
    mat = load_csv_file(path, skip)
    l = []
    for data in range(skip, len(mat)):
        item = get_data_as_dictionary_csv(data, columns)
        values = line_to_data(mapping, item)
        if values not in l:
            l.append(values)
    insert_list(l, name)


def insert_list(list, name):
    for item in list:
        insert_data(name, item.keys(), item.values())


def init_db():
    reset_all_tables()
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
    insert_xml("Données/patients.xml", PATIENT_NODE_MAPPING, "Patient")
    insert_csv(
        "Données/pathologies.csv",
        PATHOLOGIE_NODE_MAPPING,
        "Pathologie",
        ["name", "specialite"],
        0,
    )
    insert_xml("Données/diagnostiques.xml", DIAGNOSTIC_NODE_MAPPING, "Diagnostic")
    close_db(db, cursor)


if __name__ == "__main__":
    init_db()
