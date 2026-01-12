SELECT * FROM HistoricoEmprego
WHERE datatermino ISNULL
ORDER BY salario DESC
LIMIT 5;