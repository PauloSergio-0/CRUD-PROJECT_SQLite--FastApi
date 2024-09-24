from fastapi import UploadFile, HTTPException, status
import pandas as pd 



class File_manipulation:
    def __init__(self):
        self.file_path = 'data/veiculo.csv'
        self.directory = 'data'
        
        
    