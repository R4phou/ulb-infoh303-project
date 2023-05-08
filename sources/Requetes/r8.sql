SELECT path.NomPath
FROM pathologie path
JOIN diagnostic diag ON path.NomPath = diag.NomPathologie
GROUP BY path.NomPath
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*)
    FROM diagnostic diag2
    WHERE diag2.NomPathologie <> path.NomPath
    GROUP BY diag2.NomPathologie
)