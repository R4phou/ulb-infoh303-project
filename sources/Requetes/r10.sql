SELECT DISTINCT med.DCI, med.NomCom, med.systAnat
FROM Medicament med
WHERE med.NomCom in
  (SELECT dp.NomComMedicament
    FROM DossierPatient dp
    WHERE dp.datePrescription < '1999-01-01')