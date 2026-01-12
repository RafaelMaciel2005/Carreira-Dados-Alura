SELECT nome, preco
FROM produtos
GROUP BY nome,preco
HAVING preco > (
	SELECT AVG(preco)
	FROM produtos);