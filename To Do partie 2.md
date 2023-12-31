# To do

## Création --> Raph et Alex et Nico

Déduire de notre modèle relationnel un script SQL DDL de création de la base de données et de ses différentes tables ainsi que de créer cette base de données.

## Initialisation --> Alex et Nico

Ecrire un script permettant d'importer dans la base de données les données présentes dans les fichiers fournis sur l'UV. Ces données doivent être présente dans la base de données pour la défense orale.

## Requêtes

Il faut les écrires en **SQL, algèbre relationnele et calcul tuple**. Sauf la 4 et la 5 (uniquement SQL).
Il doit être possible de visualiser les résultats dans votre application.

## Délivrables

- Documents modifiés de la première partie.
- Slides reprenant une explication des méthodes d'extractions de données, les requêtes demandées et les explications et justifications de nos choix d'hypothèses.
- Une archive avec les codes sources.
  - Un fichier différent par requête
  - Un fichier pour le script DDL
  - Un fichier pour le script d'extractions de données

## Infos pratiques

- Remise le 26 mai.
- Défense orale pendant 5 à 7 minutes
  - Présenter l'application
  - Expliquer les requêtes écrites
  - Répondre aux questions
- Outils et langages de notre choix: MySQL, PostgreSQL, Python, PHP, Java
- PAS SQLite!


# à Modifier sur le schéma:

- diagnostic doit prendre un patient et non un médecin
- Médicament doit agir sur un système anatomique
- Systeme anatomique doit comprendre le nom commercial des médicament qui agissent dessus

## Mapping actuel:

Correspondance entre les fichiers et les tables actuelles:

- diagnostiques.xml -> Diagnostic
- dossier_patient.csv -> Prescription + Traitement + Medicament
- medecins.xml -> Medecin
- medicaments.csv -> Medicament
- pathologies.csv -> Pathologie
- patients.xml -> Patient
- pharmacies.xml -> Pharmacien
- specialites.xml -> SystemeAnatomique