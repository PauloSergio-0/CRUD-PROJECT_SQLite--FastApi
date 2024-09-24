from fastapi import APIRouter, UploadFile, FastAPI, File
from domain.file_processor import File_manipulation

router = APIRouter()

@router.post("/db/create")
async def test():
    return File_manipulation().Create_db()


@router.post("/db/upload")
async def upload(file: UploadFile = File(...)):
    return await File_manipulation().upload_data(file)


@router.post("/db/list_data")
async def list_all_data():
    return await File_manipulation().lista_data()