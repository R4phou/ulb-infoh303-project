SELECT distinct p.NISS, p.Lname, p.Fname
FROM DossierPatient d
JOIN Patient p ON d.NISSPatient = p.NISS
JOIN Medicament m ON d.DCI = m.DCI
WHERE d.dateVente > '1980-01-01'
AND d.NomComMedicament = 'Acinax';