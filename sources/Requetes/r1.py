def execute_requete1(dci):
    import utiles as u

    requete = (
        "SELECT NOMCOM, CONDITIONNEMENT"
        + " FROM MEDICAMENT WHERE DCI = '"
        + str(dci)
        + "'"
        + " ORDER BY NOMCOM ASC, CONDITIONNEMENT ASC;"
    )
    return u.execute_requete_with_param(requete)


if __name__ == "__main__":
    print(execute_requete1("IBUPROFENE"))
