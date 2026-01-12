SELECT id_colaborador, cargo, salario,
CASE
WHEN salario < 3000 THEN 'Baixo'
WHEN salario BETWEEN 3000 and 6000 THEN 'Médio'
ELSE 'Alto'
END AS categoria_salario
FROM HistoricoEmprego;