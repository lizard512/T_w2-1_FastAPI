from fastapi import APIRouter, UploadFile, HTTPException, Body
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import os

# 設定路由
img_router = APIRouter(prefix="/img", tags=["Image"])

# 定義Model
class ImageInfo(BaseModel):
    filename: str
    size: int

# C upload
@img_router.post("/")
async def create_upload_image(file: UploadFile):
    file_location = f"img/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    return {"filename": file.filename}

# R
@img_router.get("/{file_name}")
async def get_image(file_name: str):
    file_location = f"img/{file_name}"
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_location)

@img_router.get("/", response_model=List[ImageInfo])
async def list_uploaded_images():
    img_directory = "img/"
    try:
        files = os.listdir(img_directory)
        images_info = []
        for file in files:
            file_path = os.path.join(img_directory, file)
            size = os.path.getsize(file_path)
            images_info.append(ImageInfo(filename=file, size=size))
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Image directory not found")
    return images_info


# U name
@img_router.put("/{file_name}/{new_file_name}")
async def update_image(file_name: str, new_file_name: str):
    file_location = f"img/{file_name}"
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")
    os.rename(file_location, f"img/{new_file_name}")
    return {"msg": "File updated successfully"}


# D
@img_router.delete("/{file_name}")
async def delete_image(file_name: str):
    file_location = f"img/{file_name}"
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(file_location)
    return {"msg": "File deleted successfully"}
