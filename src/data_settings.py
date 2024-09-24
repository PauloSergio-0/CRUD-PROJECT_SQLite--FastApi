import sqlite3 as con


sql_carros = """
    CREATE TABLE IF NOT EXISTS Veiculo (
    Id_Veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    Marca_Veiculo VARCHAR(40) NOT NULL,
    Modelo_Veiculo VARCHAR(40) NOT NULL,
    Preco_Veiculo DECIMAL(10,2) NOT NULL,
    Ano_Veiculo INTEGER,
    Qtde_estoque SMALLINT NOT NULL
    );
"""

sql_clientes = """
    CREATE TABLE IF NOT EXISTS Cliente (
    Id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    RG VARCHAR (12) NOT NULL,
    Nome_cliente VARCHAR(30) NOT NULL,
    Sobrenome_cliente VARCHAR(40) NOT NULL,
    Telefone VARCHAR(12),
    Rua VARCHAR(40),
    Numero VARCHAR(5),
    Bairro VARCHAR(25)
    );
"""

sql_vendas = """
    CREATE TABLE IF NOT EXISTS Venda (
    ID_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    Nota_Fiscal SAMLLINT NOT NULL,
    ID_Cliente INTEGER NOT NULL,
    Data_compra DATETIME,
    ID_Veiculo INTEGER NOT NULL,
    Quantidade SAMLLINT NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(Id_Cliente),
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(Id_Veiculo)
    );
"""

def make_db():
    try:
        global Conexao
        Conexao = con.connect("src/data/concessionaria.db")
        global curso
        curso = Conexao.cursor()
        
        curso.execute(sql_carros)
        curso.execute(sql_clientes)
        curso.execute(sql_vendas)
        
        Conexao.commit()
        
    except con.DatabaseError as e:
        print(f'Ocorreu um erro: {e}')
    # finally:
    #     if Conexao:
    #         Conexao.close()
            
def verificar_db():
    
    try:
        res = curso.execute("SELECT name FROM sqlite_master")
        print(res.fetchall())
    except con.DatabaseError as e:
        print(f'Ocorreu um erro: {e}')

def insert_vendas (Nota_Fiscal, Id_cliente, Data_compra, Id_Veiculo, Quantidade):
    
    try:
        curso.execute(f"""INSERT INTO Venda (Nota_Fiscal, ID_Cliente, Data_compra, ID_Veiculo, Quantidade)
                        VALUES (?,?,?,?,?)""", (Nota_Fiscal, Id_cliente, Data_compra, Id_Veiculo, Quantidade))
        Conexao.commit()
    except con.DatabaseError as e:
        print(f"Erro: {e}")

def inserir_dados_vendas():
    inserer_vendas = """
    INSERT INTO Venda (Nota_Fiscal, ID_Cliente, Data_compra, ID_Veiculo, Quantidade) 
    VALUES 
    (123, 2, '2024-12-08', 2, 1),
    (123, 1, '2024-12-08', 3, 1),
    (123, 3, '2024-12-08', 1, 3),
    (123, 4, '2024-12-08', 2, 1);
    """
    
    try:
        curso.execute(inserer_vendas)
        
        Conexao.commit()
        
    except con.DatabaseError as e:
        print(f'Ocorreu um erro: {e}')
        
        
def inserir_dados_carros():
    insere_carro = """
    INSERT INTO Veiculo (Marca_Veiculo, Modelo_Veiculo, Preco_Veiculo, Ano_Veiculo, Qtde_estoque) VALUES 
    ('Ferrari', 'Enzo', 123.67, 1992, 23),
    ('Ferrari', 'La_Ferrari', 167.90, 1962, 3),
    ('Porshe', '911s', 902.22,1990, 8);
    """
    try:
        curso.execute(insere_carro)
        Conexao.commit()
    except con.DatabaseError as e:
        print(f"Ocorreu um erro: {e}")
        

def inserir_dados_Clientes():
    insere_cliente  = """
        INSERT INTO Cliente (RG, Nome_cliente, Sobrenome_cliente , Telefone, Rua, Numero, Bairro) VALUES 
        ('12345678901', 'Carlos', 'Silva', '1234567890', 'Rua das Flores', '123', 'Centro'),
        ('98765432109', 'Ana', 'Souza', '0987654321', 'Avenida Brasil', '456', 'Jardim América'),
        ('56789012345', 'Marcos', 'Pereira', '1122334455', 'Rua dos Pinheiros', '789', 'Vila Nova'),
        ('23456789012', 'Luana', 'Oliveira', '2345678901', 'Rua das Laranjeiras', '321', 'Bela Vista'),
        ('34567890123', 'Ricardo', 'Martins', '3456789012', 'Avenida das Palmeiras', '654', 'Jardim São Paulo'),
        ('45678901234', 'Fernanda', 'Alves', '4567890123', 'Praça da Liberdade', '987', 'Centro Histórico'),
        ('56789012346', 'Tiago', 'Gomes', '5678901234', 'Rua do Comércio', '852', 'Vila Esperança');
    """
    try:
        curso.execute(insere_cliente)
        Conexao.commit()
    except con.DatabaseError as e:
        print(f'Ocorreu um erro: {e}')


def listar_dados(tabela = 'Cliente'):
    listar_tabela = f"SELECT * FROM {tabela};"
    try:
        curso.execute(listar_tabela)
        res = curso.fetchall()
        for row in res:
            print(row)
    except con.DatabaseError as e:
        print(f'Ocorreu um erro: {e}')
        

make_db() 
# verificar_db()
# inserir_dados_Clientes()
# inserir_dados_carros()
# inserir_dados_vendas()

insert_vendas(Nota_Fiscal=123, Id_cliente=2, Data_compra="2024-10-05", Id_Veiculo=3, Quantidade=1)
listar_dados(tabela='Venda')

global Conexao
if Conexao:
    Conexao.close()