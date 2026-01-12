CREATE VIEW ViewValorTotalPedido AS
SELECT p.id, c.nome, p.datahorapedido, SUM(ip.precounitario) AS ValorTotalPedido
FROM clientes c
JOIN pedidos p
		ON c.id = p.idcliente
JOIN itenspedidos ip
		ON p.id = ip.idpedido
GROUP BY p.id, c.nome;