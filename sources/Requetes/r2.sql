SELECT p.NomPath, p.NomSpec
  FROM pathologie p
  WHERE p.NomSpec IN 
    (SELECT NomSpec 
    FROM specsystanat 
    GROUP BY NomSpec 
    HAVING COUNT(DISTINCT NomSystAnat) = 1)