INSERT INTO tabela_pedidos_gold(
	id_pedido_gold,
  	data_do_pedido_gold,
  	status_gold,
  	total_do_pedido_gold,
  	cliente_gold,
  	data_de_envio_estimada_gold
)
SELECT 
	id,
    data_do_pedido,
    status,
    total_do_pedido,
    cliente,
    data_de_envio_estimada
FROM tabelapedidos
WHERE total_do_pedido >= 400;