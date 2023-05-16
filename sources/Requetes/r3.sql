SELECT Medecin.Speciality, COUNT(DossierPatient.NomComMedicament) AS PrescriptionCount
FROM Medecin
JOIN DossierPatient ON Medecin.INAMI = DossierPatient.InamiMed
GROUP BY Medecin.Speciality
ORDER BY PrescriptionCount DESC
LIMIT 1;