SELECT p.NomPath
FROM pathologie p
GROUP BY NomPath
HAVING COUNT(NomSpec)=1