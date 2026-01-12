CREATE TABLE itenspedidos (
  idpedido TEXT,
  idproduto TEXT,
  quantidade INTEGER,
  precounitario DECIMAL(10,2),
  PRIMARY KEY (idpedido,idproduto),
  FOREIGN KEY (idpedido) REFERENCES pedidos(id) ON DELETE CASCADE,
  FOREIGN KEY (idproduto) REFERENCES produtos(id) ON DELETE CASCADE
)