SELECT t2.nom, t2.decennie, t2.c
FROM(
        SELECT t1.nom, t1.decennie, t1.c, MAX(t1.c) OVER (PARTITION BY (t1.decennie)) AS m2
        FROM (
                SELECT m.`NomCom` AS nom, floor(YEAR(p.`Bdate`)/10)*10 AS decennie, COUNT(m.`DCI`) c
                FROM patient p JOIN dossierpatient dossier ON dossier.`NISSPatient` = p.`NISS`
                JOIN medicament m ON m.`DCI` = dossier.`DCI`
                GROUP BY nom,decennie HAVING (decennie >= 1950 AND decennie < 2020)
        ) AS t1
) AS t2
WHERE t2.c = t2.m2
ORDER BY decennie ASC;