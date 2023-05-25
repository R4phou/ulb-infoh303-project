def execute_requete4(date, nomComMedicament):
    import utiles as u

    requete = (
        "SELECT distinct p.NISS, p.Lname, p.Fname"
        + " FROM DossierPatient d"
        + " JOIN Patient p ON d.NISSPatient = p.NISS"
        + " JOIN Medicament m ON d.DCI = m.DCI"
        + " WHERE d.dateVente > '"
        + str(date)
        + "'"
        + " AND d.NomComMedicament = '"
        + str(nomComMedicament)
        + "'"
    )
    return u.execute_requete_with_param(requete)
