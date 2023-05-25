def get_donnees_patient(niss):
    import utiles as u
    query = (
        "SELECT `NomMed`,`NomPhar`,`InamiMed`,`InamiPhar`,`NomComMedicament`,`DCI`,`datePrescription`,`dateVente`,`dureeTraitement` "
        + "FROM dossierpatient "
        + "WHERE `NISSPatient` ="
        + str(niss)
    )
    return u.execute_requete_with_param(query)

if __name__ == "__main__":
    print(get_donnees_patient(2017845529))