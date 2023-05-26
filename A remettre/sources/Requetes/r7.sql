SELECT T2.NOM, T2.DECENNIE, T2.C
FROM(
                SELECT T1.NOM, T1.DECENNIE, T1.C, MAX(T1.C) OVER (
                        PARTITION BY (T1.DECENNIE)) AS M2
                FROM (
                                SELECT M.NOMCOM AS NOM, FLOOR(YEAR(P.BDATE)/10)*10 AS DECENNIE, COUNT(M.DCI) C
                                FROM PATIENT P, DOSSIERPATIENT DP, MEDICAMENT M
                                WHERE DP.NISSPATIENT = P.NISS AND
                                        M.DCI = DP.DCI
                                GROUP BY NOM, DECENNIE
                                HAVING (DECENNIE >= 1950 AND
                                        DECENNIE < 2020)
                        ) AS T1
        ) AS T2
WHERE T2.C = T2.M2
ORDER BY DECENNIE ASC;