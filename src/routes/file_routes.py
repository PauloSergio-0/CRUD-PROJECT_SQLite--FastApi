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
async def filter_all_data(marca_veiculo: str = None, modelo_veiculo: str = None, preco_veiculo: float = None, qtde_veiculo: int = None):
    data_filter = {
        k: v for k, v in {
        "marca": marca_veiculo,
        "modelo": modelo_veiculo,
        "preco": preco_veiculo,
        "qtde": qtde_veiculo,
        }.items() 
        if v is not None
        }
    print(data_filter)
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

    data_v= {}
    
    if marca_veiculo:
        data_v["marca"] = marca_veiculo
        
        
    if modelo_veiculo:
        data_v["modelo"] = modelo_veiculo
    
    return await File_manipulation().delete_data(data_v)

@router.post("/db/update")
async def update(marca_veiculo: str, modelo_veiculo: str, new_marca_veiculo: str = None, new_modelo_veiculo: str = None,new_preco_veiculo: float = None, new_qtde_veiculo: int = None):
    
    
    data_update = {
        k: v for k, v in {
            "new_marca": new_marca_veiculo,
            "new_modelo": new_modelo_veiculo,
            "new_preco": new_preco_veiculo,
            "new_qtde": new_qtde_veiculo,
            "marca": marca_veiculo,
            "modelo": modelo_veiculo
        }.items() 
        if v is not None}

    return await File_manipulation().update_data(data_update)