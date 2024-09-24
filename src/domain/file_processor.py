from fastapi import UploadFile, HTTPException, status
import pandas as pd 
import sqlite3 as con


class File_manipulation:
    def __init__(self):
        self.file_path = 'data/veiculo.db'
        self.directory = 'data'
        
        
    def Create_db(self):
        sql_create = """
        CREATE TABLE IF NOT EXISTS Carro (
            
        )
        """