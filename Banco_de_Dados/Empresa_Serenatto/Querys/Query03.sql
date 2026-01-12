SELECT c.nome, p.id, p.datahorapedido
FROM clientes c
INNER JOIN pedidos p
ON c.id = p.idcliente;