SELECT instituicao, COUNT(curso)
FROM Treinamento
GROUP BY instituicao
HAVING COUNT(curso) > 2;