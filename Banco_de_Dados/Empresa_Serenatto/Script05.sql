CREATE TABLE pedidos (
  id TEXT PRIMARY KEY,
  idcliente TEXT,
  datahorapedido DATETIME,
  status VARCHAR(50),
  FOREIGN KEY (idcliente) REFERENCES clientes(id) ON DELETE CASCADE
);