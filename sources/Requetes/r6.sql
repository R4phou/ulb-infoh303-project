SELECT DISTINCT M.LNAME, M.INAMI
FROM MEDECIN M
WHERE M.INAMI IN (
        SELECT DP.INAMIMED
        FROM DOSSIERPATIENT DP
        WHERE DP.NOMCOMMEDICAMENT IN (
                SELECT MED.NOMCOM
                FROM MEDICAMENT MED
                WHERE MED.SYSTANAT IN (
                        SELECT S.NOMSYSTANAT
                        FROM SPECSYSTANAT S
                        WHERE S.NOMSPEC NOT IN (
                                SELECT M2.SPECIALITY
                                FROM MEDECIN M2
                                WHERE M2.INAMI = M.INAMI
                            )
                    )
            )
    )