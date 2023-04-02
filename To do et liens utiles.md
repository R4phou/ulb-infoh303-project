
# Liens:

- Schéma ER: https://drive.google.com/file/d/1EY6zpli7nDDFRm-1vhLvtrn7uamu1e9f/view?usp=sharing

# TO DO
## A déposer sur l'UV pour le 5 avril

- Rapport
  - Diagramme entité association
  - Contraintes

  - Traduction relationnelle du diagramme et des contraintes

  - Hypothèses et justification des choix de modélisation

# Résumé du texte
Dossier patient permet au professionel d'accéder aux infos d'un patient
## Entités
- Patient
  - **Numéro d'identification (NISS)**
  - Permet de l'identifier dans les procédures liées à la sécurité sociale
  - Nom
  - Prénom
  - Genre
  - Date de naissance
  - (Adresse mail)
  - (Numéro de téléphone)

- DossierPatient

- Médecin et Pharmacien
  - **Numéro INAMI**
  - Numéro de téléphone
  - Adresse mail


- Médecin

- Pathologie
  - Date de diagnostic

- Système anatomique
- Prescription
  - Nom commercial de médicament (NomMedicament)
  - INAMI du médecin (INAMIM)
  - Nom du médecin (NomMedecin)
  - Durée du traitement (Durée)

- Médicament
  - **Nom commercial**
  - Nom de molécule active (DCI)
  - Conditionnement (nombre de comprimés dans la boîte)


- Traitement
  - Plusieurs Médicaments (1, n)
  - Nom prescripteur (NomP)
  - Numéro INAMI prescripteur (INAMIP)
  - Nom du pharmacien (NomPharma)
  - Date de début
  - Durée


## Relations
- Patient a un dossierPatient
- Patient a un médecin (contact en cas de problème)
- Paritent a un pharmacien de référence (contact en cas de problèmes)
- Médecin se spécialise à un système anatomique
- Pathologie dans le dossier du patient
- DossierPatient contient pathologie
- Pathologie associée à un système anatomique
- Médecin fait une Prescription
- Pharmacien lié à Médicament via Prescription
- Patient a un Traitement
## Contraintes 
- INAMI et nom du médecin dans prescription
- Pharmacien choisit le conditionnement le plus petit pour couvrir la durée du traitement




