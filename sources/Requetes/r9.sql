SELECT p.LName, p.Fname, COUNT(DISTINCT dp.InamiMed)
FROM DossierPatient dp, Patient p
WHERE dp.NISSPatient = p.NISS
GROUP BY p.LName, p.Fname