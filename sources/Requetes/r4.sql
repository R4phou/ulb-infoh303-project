SELECT Patient.NISS, Patient.Lname, Patient.Fname
FROM DossierPatient
JOIN Patient ON DossierPatient.NISSPatient = Patient.NISS
JOIN Medicament ON DossierPatient.DCI = Medicament.DCI
WHERE Medicament.NomCom = 'nom_du_medicament'
AND DossierPatient.dateVente > 'date_donnee';