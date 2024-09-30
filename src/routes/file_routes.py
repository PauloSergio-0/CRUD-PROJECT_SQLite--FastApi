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
async def filter_all_data(marca_veiculo: str=None, modelo_veiculo: str = None, preco_veiculo: float= None, qtde_veiculo: int= None):
    data_filter = {}

    if marca_veiculo:
        data_filter["marca"] = marca_veiculo

    if modelo_veiculo:
        data_filter["modelo"]= modelo_veiculo

    if preco_veiculo:
        data_filter["preco"]= preco_veiculo

    if qtde_veiculo:
        data_filter["qtde"] = qtde_veiculo

    print(test)
    return await File_manipulation().Filter_table(data_filter)


@router.post("/db/insert_data")
async def insert(marca_veiculo: str, modelo_veiculo: str, preco_veiculo: float, qtde_veiculo: int):
    data_veiculo = dict(
                Marca = marca_veiculo,
                Modelo = modelo_veiculo,
                Preco = preco_veiculo,
                Qtde = qtde_veiculo
                        )
    return await File_manipulation().insert_data(data_veiculo)

@router.delete("/db/delete_data")
async def delete_data(marca_veiculo: str, modelo_veiculo: str):

    data_v= dict(marca= marca_veiculo,modelo = modelo_veiculo)
    return await File_manipulation().delete_data(data_v)