SELECT * FROM pessoas; 


INSERT INTO pessoas (nome, idade, email) VALUES("hirohito", 58, "japam@jpa.com"),
  ("stalin", 23, "urrs@gmail.com");


DELETE FROM  pessoas WHERE idade = 25;

SELECT * FROM  pessoas WHERE email LIKE "%gmail.com";


SELECT rowid,* FROM pessoas WHERE idade > 19 AND email LIKE "%@gmail.com"; 


SELECT * FROM Cliente ORDER BY Nome_cliente ASC , Sobrenome_cliente DESC; 

SELECT  * FROM  Cliente;

SELECT * FROM Venda;

SELECT  * FROM Veiculo WHERE Marca_Veiculo = 'Ferrari';

SELECT  * FROM Veiculo WHERE Marca_Veiculo LIKE "Fer%";


UPDATE Veiculo SET Marca_Veiculo = "Porshe" WHERE Marca_Veiculo = "Proshe";

PRAGMA table_info(Veiculo); /* lista todas as colunas*/

PRAGMA table_info(Venda);

INSERT INTO Cliente(RG, Nome_cliente, Sobrenome_cliente, Telefone, Rua, Numero, Bairro) VALUES ('11156789012', 'Lua', 'Oliveira', '2895678901', 'Rua das Laranjeiras', '321', 'Bela Vista');