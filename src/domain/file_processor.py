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
            
            
    async def Filter_table(self, data: dict):
        print(data)
        sql_filter = """SELECT * FROM Carro"""

        condicoes = []

        if ("marca" in data) and  (data["marca"] is not None):
            condicoes.append("Marca_veiculo = ?")
            
        if ("modelo" in data) and  (data["modelo"] is not None):
            condicoes.append("Modelo_carro = ?")
            
        if ("preco" in data) and (data["preco"] is not None):
            condicoes.append("Preco_carro <= ?")
        
        if ("qtde" in data) and (data["qtde"] is not None):
            condicoes.append("Qtde_carro <= ?")
            
        if condicoes:
            sql_filter += " WHERE "+" AND ".join(condicoes)
        print(sql_filter)
        dado_filter = []
        try:
            self.cursor.execute(sql_filter, tuple(data.values()))
            dado = self.cursor.fetchall()
            
            for item in dado:
                content = dict(ID_veiculo = item[0], marca_veiculo = item[1], modelo_veiculo= item[2], preco_veiculo=item[3], qtde_veiculo = item[4])
                dado_filter.append(content)
            return {"data": dado_filter}
        except con.DatabaseError as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                                detail = f"Erro: {e}")
                
                
    async def insert_data(self, data: dict):
        sql_insert_data = """
        INSERT INTO Carro 
        (Marca_veiculo, Modelo_carro, Preco_carro, Qtde_carro) 
        VALUES (?, ?, ?, ?)
        """
        try:
            self.cursor.execute(sql_insert_data, tuple(data.values()))
            self.conexao.commit()
            return {"menssagen": "dados inseridos com sucesso"}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=f'erro: {e}')
        finally:
            self.close_db()
            
            
        
    async def delete_data(self, data: dict):
        sql_delete = """
        DELETE FROM Carro 
        WHERE Marca_veiculo = ? AND Modelo_carro = ?
        """


        try: 
            self.cursor.execute(sql_delete, tuple(data.values()))
            self.conexao.commit()
            self.close_db()
            return {"menssage": "Deletado com sucesso"}
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f'erro: {e}')