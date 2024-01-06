from fastapi import FastAPI, File, UploadFile
from ml_obj_detection import detect

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    out_response = detect(file.file)

    return {"objects": out_response}
