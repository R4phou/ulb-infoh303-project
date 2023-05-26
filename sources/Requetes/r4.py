def execute_requete4(date, nomComMedicament):
    import utiles as u

    requete = (
        "SELECT distinct p.NISS, p.Lname, p.Fname"
        + " FROM DossierPatient d, Patient p, Medicament m"
        + " WHERE d.NISSPatient = p.NISS"
        + " AND d.DCI = m.DCI"
        + " AND d.dateVente > '"
        + str(date)
        + "'"
        + " AND d.NomComMedicament = '"
        + str(nomComMedicament)
        + "'"
    )
    return u.execute_requete_with_param(requete)
