from fastapi import UploadFile, HTTPException, status
import pandas as pd 
import sqlite3 as con
from io import StringIO

class File_manipulation:
    def __init__(self):
        self.file_path = 'src/data/veiculo.db'
        self.conexao = con.connect(self.file_path)
        self.cursor = self.conexao.cursor()
        
        
    def close_db(self):
        
        try:
            self.conexao.close()
        except con.DatabaseError as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Erro ao fechar conexão: {e}")
            
    def Create_db(self):
        sql_create = """
        CREATE TABLE IF NOT EXISTS Carro (
            Id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
            Marca_veiculo VARCHAR(40) NOT NULL,
            Modelo_carro VARCHAR(40) NOT NULL,
            Preco_carro FLOAT NOT NULL,
            Qtde_carro INTEGER NOT NULL
        )
        """
        
        try:
            self.cursor.execute(sql_create)
            self.conexao.commit()
            self.close_db()
            return {"menssage": "banco criado com sucesso!!!"}
        
        except con.DatabaseError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"falhas: {str(e)}")
    
    
    def insert_db(self, data: list):
        sql_insert ="""
        INSERT INTO Carro (Marca_veiculo, Modelo_carro, Preco_carro, Qtde_carro) VALUES (?, ?, ?, ?)
        """
        
        try:
            for item in data:
                
                self.cursor.execute(sql_insert, item)
            self.conexao.commit()
            
        except con.DatabaseError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"falhas: {str(e)}")
    
    
    async def upload_data(self, File: UploadFile):
        if File.filename.endswith(".csv"):
            try:
                sql_tuple = []
                
                file_content = await File.read()
                
                data = pd.read_csv(StringIO(file_content.decode('utf-8')), sep=",", 
                dtype={
                'Marca_veiculo':'string', 
                'Modelo_carro': 'string',
                'Preco_carro': 'float64',
                'Qtde_carro': 'int32'
                })
                
                for _, row in data.iterrows():
                    content = (row[0], row[1], row[2], row[3])
                    
                    sql_tuple.append(content)
                self.insert_db(sql_tuple)
                self.close_db()
                return {"menssage": sql_tuple}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"falhas: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Não é csv: {str(e)}")
            
            
    async def lista_data(self):
        dados_menssage= []
        try:
            self.cursor.execute("SELECT * FROM Carro")
            dados = self.cursor.fetchall()
            for row in dados:
                content = dict(id=row[0], Marca = row[1], Modelo = row[2], Preco = row[3], Quantidade = row[4])
                dados_menssage.append(content)
                
            self.close_db()
            return {"menssagen": dados_menssage}
        except con.DatabaseError as e:
            print(f"Erro a acessar banco de dados: {e}")