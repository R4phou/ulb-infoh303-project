SELECT LNAME, FNAME
FROM PATIENT
WHERE NISS IN (
    SELECT DISTINCT DP.NISSPATIENT
    FROM DOSSIERPATIENT DP
    WHERE DP.DATEVENTE < DATE_SUB(CURRENT_DATE(), INTERVAL DP.DUREETRAITEMENT DAY) AND
      NOT EXISTS (
        SELECT 1
        FROM DOSSIERPATIENT DP2
        WHERE DP2.NISSPATIENT = DP.NISSPATIENT AND
          DP2.NOMCOMMEDICAMENT = DP.NOMCOMMEDICAMENT AND
          DP2.DATEVENTE >= DATE_SUB(CURRENT_DATE(), INTERVAL DP2.DUREETRAITEMENT DAY)
      )
  )