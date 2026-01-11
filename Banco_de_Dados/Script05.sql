CREATE TABLE tabelaprodutos(
	ID_Produto INT PRIMARY KEY,
  	Nome_do_Produto VARCHAR (250),
  	Descricao TEXT,
  	Categoria INT,
  	Preco_de_compra DECIMAL (10,2),
  	Unidade Varchar (50),
  	Fornecedor INT,
  	Data_de_Inclusao DATE,
  	FOREIGN KEY (Categoria) REFERENCES tabelacategorias(id_categoria),
  	FOREIGN KEY (Fornecedor) REFERENCES tabelafornecedores(id)
);