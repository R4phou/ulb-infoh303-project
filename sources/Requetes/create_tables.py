#Définition des requêtes de création des tables

#Les numéros inami sont mis en VARCHAR car les valeurs sont supérieures à 2^32
patient_query = """CREATE TABLE Patient 
    (NISS VARCHAR(50) PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Fname VARCHAR(50) NOT NULL,
    Bdate DATE NOT NULL,
    Email VARCHAR(50),
    Phone VARCHAR(50),
    INAMImed VARCHAR(50) NOT NULL,
    INAMIphar VARCHAR(50) NOT NULL)"""

medecin_query = """CREATE TABLE Medecin
    (
    INAMI INT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone INT,
    Speciality VARCHAR(50)
    )
"""

pharmacien_query = """CREATE TABLE Pharmacien
    (INAMI INT PRIMARY KEY,
    Lname VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone INT)
"""

medicament_query = """CREATE TABLE Medicament
    (
    NameMedicament VARCHAR(50) PRIMARY KEY,
    DCI VARCHAR(50) NOT NULL,
    Quantity INT NOT NULL)
"""

anat_system_query = """CREATE TABLE AnatSystem
    (NameAnatSystem VARCHAR(50) PRIMARY KEY)
"""

pathologie_query = """CREATE TABLE Pathologie
    (
    NamePathologie VARCHAR(50) PRIMARY KEY,
    NameAnatSystem VARCHAR(50) NOT NULL,
    FOREIGN KEY(NameAnatSystem) REFERENCES AnatSystem(NameAnatSystem))
"""
traitement_query = """CREATE TABLE Traitement
    (
    NameTrait VARCHAR(50) PRIMARY KEY,
    DateBegin DATE NOT NULL,
    Duration INT NOT NULL,
    NISSPatient VARCHAR(50) NOT NULL,
    FOREIGN KEY (NISSPatient) REFERENCES Patient(NISS))
"""
traitement_pathologie_query = """CREATE TABLE TraitementPathologie
    (
    NameTrait VARCHAR(50) NOT NULL,
    NamePath VARCHAR(50) NOT NULL,
    FOREIGN KEY (NameTrait) REFERENCES Traitement(NameTrait),
    FOREIGN KEY (NamePath) REFERENCES Pathologie(NamePathologie))
"""
diagnostic_query = """CREATE TABLE Diagnostic
    (NISSPatient VARCHAR(50) NOT NULL,
    NomPathologie VARCHAR(50) NOT NULL,
    NomTraitement VARCHAR(50) NOT NULL,
    FOREIGN KEY (NISSPatient) REFERENCES Patient(NISS),
    FOREIGN KEY (NomPathologie) REFERENCES Pathologie(NamePathologie),
    FOREIGN KEY (NomTraitement) REFERENCES Traitement(NameTrait),
    DiagnosticDate DATE NOT NULL)
"""

#Permet de récupérer les requêtes sous forme de liste.
def get_table_creation_queries():
    return [patient_query,medecin_query,pharmacien_query,medicament_query,anat_system_query,pathologie_query,traitement_query,traitement_pathologie_query,diagnostic_query]