# Ordre d'insertion des données du patient dans la base de données
PATIENT_NODE_MAPPING = {
    "NISS": "NISS",
    "nom": "Lname",
    "prenom": "Fname",
    "date_de_naissance": "Bdate",
    "mail": "Email",
    "telephone": "Phone",
    "inami_medecin": "INAMImed",
    "inami_pharmacien": "INAMIphar",
}

# Ordre d'insertion des données du médecin dans la base de données
MEDECIN_NODE_MAPPING = {
    "inami": "INAMI",
    "nom": "Lname",
    "mail": "Email",
    "telephone": "Phone",
    "specialite": "Speciality",
}

# Ordre d'insertion des données du pharmacien dans la base de données
PHARMACIEN_NODE_MAPPING = {
    "inami": "INAMI",
    "nom": "Lname",
    "mail": "Email",
    "tel": "Phone",
}

# Ordre d'insertion des données du diagnostique dans la base de données
DIAGNOSTIC_NODE_MAPPING = {
    "naissance": "BirthDate",
    "pathology": "NomPathologie",
    "NISS": "NISSPatient",
    "date_diagnostic": "date",
    "specialite": "NomSpec",
}

SPECIALITE_NODE_MAPPING = {"name": "NomSpec", "medicament": "NomSystAnat"}


MEDICAMENT_NODE_MAPPING = {
    "dci": "DCI",
    "nom Commercial": "NomCom",
    "système anatomique": "systAnat",
    "conditionnement": "Conditionnement",
}

PATHOLOGIE_NODE_MAPPING = {"name": "NomPath", "specialite": "NomSpec"}


DOSSIER_NODE_MAPPING = {
    "NISS_patient": "NISSPatient",
    "medecin": "NomMed",
    "inami_medecin": "INAMImed",
    "pharmacien": "NomPhar",
    "inami_pharmacien": "INAMIphar",
    "medicament_nom_commercial": "NomComMedicament",
    "DCI": "DCI",
    "date_prescription": "datePrescription",
    "date_vente": "dateVente",
    "duree_traitement": "dureeTraitement",
}
