CREATE TABLE clientes (
  id TEXT NOT NULL,
  nome VARCHAR(255),
  telefone VARCHAR(20),
  email VARCHAR(100) DEFAULT 'Sem email',
  endereco VARCHAR(255),
  PRIMARY KEY (id)
);