def execute_requete10(date):
    import utiles as u

    requete = (
        "SELECT DISTINCT MED.DCI, MED.NOMCOM, MED.SYSTANAT"
        + " FROM MEDICAMENT MED"
        + " WHERE MED.NOMCOM IN ("
        + " SELECT DP.NOMCOMMEDICAMENT"
        + " FROM DOSSIERPATIENT DP"
        + " WHERE DP.DATEPRESCRIPTION < '"
        + str(date)
        + "');"
    )
    return u.execute_requete_with_param(requete)
