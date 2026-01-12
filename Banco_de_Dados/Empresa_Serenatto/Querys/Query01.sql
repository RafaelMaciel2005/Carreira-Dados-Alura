SELECT nome, telefone
FROM clientes
WHERE id = (
	SELECT idcliente
	FROM pedidos
	WHERE datahorapedido = '2023-01-02 08:15:00');