from fastapi import APIRouter, UploadFile, FastAPI, File
from domain.file_processor import File_manipulation

router = APIRouter()

@router.post("/db/create")
async def test():
    return File_manipulation().Create_db()


@router.post("/db/upload")
async def upload(file: UploadFile = File(...)):
    return await File_manipulation().upload_data(file)


@router.get("/db/list_data")
async def list_all_data():
    return await File_manipulation().lista_data()


@router.get("/db/filter_data")
async def filter_all_data(marca_veiculo: str):
    return await File_manipulation().Filter_table(marca_veiculo)

@router.get("/db/insert_data")
async def insert_data(marca_veiculo: str, modelo_veiculo: str, preco_veiculo: float, Qtde_veiculo: int):
    data_veiculo = dict(Marca = marca_veiculo, Modelo = modelo_veiculo, Preco = preco_veiculo, Qtde = Qtde_veiculo)
    return await File_manipulation().insert_data(data_veiculo)

@router.get("/db/delete_data")
async def delete(marca_veiculo: str, modelo_veiculo: str):

    data_v= dict(marca= marca_veiculo,modelo = modelo_veiculo)
    return await File_manipulation().delete_data(data_v)