# Définition des requêtes de création des tables

# Les numéros inami sont mis en VARCHAR car les valeurs sont supérieures à 2^32
medecin_query = """CREATE TABLE Medecin
    (
    INAMI BIGINT NOT NULL PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone VARCHAR(50),
    Speciality VARCHAR(50) NOT NULL,
    FOREIGN KEY (Speciality) REFERENCES SpecSystAnat(NomSpec)
    )
"""

pharmacien_query = """CREATE TABLE Pharmacien
    (INAMI BIGINT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone VARCHAR(50))
"""

patient_query = """CREATE TABLE Patient 
    (NISS BIGINT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Fname VARCHAR(50) NOT NULL,
    Bdate DATE NOT NULL,
    Email VARCHAR(50),
    Phone VARCHAR(50),
    INAMImed BIGINT NOT NULL,
    INAMIphar BIGINT NOT NULL
    )"""

speciality_query = """CREATE TABLE SpecSystAnat
    (
    NomSpec VARCHAR(50) NOT NULL,
    NomSystAnat VARCHAR(100) NOT NULL,
    PRIMARY KEY (NomSpec, NomSystAnat)
    )
"""

medicament_query = """CREATE TABLE Medicament
    (
    DCI VARCHAR(50) NOT NULL,
    NomCom VARCHAR(50) NOT NULL,
    systAnat VARCHAR(100) NOT NULL,
    Conditionnement INT NOT NULL,
    PRIMARY KEY (DCI, NomCom, systAnat, Conditionnement)
    )
"""

pathologie_query = """CREATE TABLE Pathologie
    (
    NomPath VARCHAR(50) PRIMARY KEY,
    NomSpec VARCHAR(50) NOT NULL,
    FOREIGN KEY (NomSpec) REFERENCES SpecSystAnat(NomSpec)
    )
"""

diagnostic_query = """CREATE TABLE Diagnostic
    (
    NISSPatient BIGINT NOT NULL,
    BirthDate DATE NOT NULL,
    date DATE NOT NULL,
    NomSpec VARCHAR(50) NOT NULL,
    NomPathologie VARCHAR(50) NOT NULL PRIMARY KEY,
    FOREIGN KEY (NISSPatient) REFERENCES Patient(NISS),
    FOREIGN KEY (NomSpec) REFERENCES SpecSystAnat(NomSpec),
    FOREIGN KEY (NomPathologie) REFERENCES Pathologie(NomPath))
"""

dossier_patient_query = """CREATE TABLE DossierPatient
    (
    NISSPatient BIGINT NOT NULL,
    NomMed VARCHAR(50) NOT NULL,
    NomPhar VARCHAR(50) NOT NULL,
    InamiMed BIGINT NOT NULL,
    InamiPhar BIGINT NOT NULL,
    NomComMedicament VARCHAR(50) NOT NULL,
    DCI VARCHAR(50) NOT NULL,
    datePrescription DATE NOT NULL,
    dateVente DATE NOT NULL,
    dureeTraitement INT NOT NULL,
    FOREIGN KEY (NISSPatient) REFERENCES Patient(NISS),
    FOREIGN KEY (InamiMed) REFERENCES Medecin(INAMI),
    FOREIGN KEY (InamiPhar) REFERENCES Pharmacien(INAMI),
    FOREIGN KEY (DCI) REFERENCES Medicament(DCI))
"""

# Permet de récupérer les requêtes sous forme de liste.


def get_table_creation_queries():
    # , pathologie_query, diagnostic_query, dossier_patient_query]
    return [
        speciality_query,
        medecin_query,
        pharmacien_query,
        patient_query,
        medicament_query,
        pathologie_query,
        diagnostic_query,
        dossier_patient_query,
    ]
