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
    
            
def verificar_db():
    
    try:
        res = curso.execute("SELECT * FROM sqlite_master")
        print(res.fetchall())
    except con.DatabaseError as e:
        print(f'Ocorreu um erro: {e}')


make_db()
verificar_db()

global Conexao
if Conexao:
    Conexao.close()