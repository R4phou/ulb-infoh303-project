
SELECT m.`NomCom` AS nom, floor(YEAR(p.`Bdate`)/10)*10 AS decennie, COUNT(m.`DCI`) c
        FROM patient p JOIN dossierpatient dossier ON dossier.`NISSPatient` = p.`NISS`
        JOIN medicament m ON m.`DCI` = dossier.`DCI`
        GROUP BY nom, decennie HAVING (decennie >= 1950 AND decennie < 2020)
        ORDER BY decennie ASC;
