from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

## hooks
def setup_module(module):
    os.makedirs("img", exist_ok=True)

# def teardown_module(module):
#     test_files = ["test_image.png", "new_name.png"]
#     for file in test_files:
#         file_path = os.path.join("img", file)
#         os.remove(file_path)

## test cases
def test_create_upload_image():
    response = client.post("/img/", files={"file": ("test_image.png", b"fakeimagecontent")})
    assert response.status_code == 200
    assert response.json()["filename"] == "test_image.png"

def test_get_image():
    # existing image
    response = client.get("/img/test_image.png")
    assert response.status_code == 200
    # non-existent image
    response = client.get("/img/non_existent_image.png")
    assert response.status_code == 404
    assert response.json() == {"detail": "File not found"}

def test_list_uploaded_images():
    response = client.get("/img/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    # simulate a non-existent directory
    os.rename("img", "img_backup")
    response = client.get("/img/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Image directory not found"}
    # recover after testing
    os.rename("img_backup", "img")

def test_update_image():
    # existing image
    response = client.put("/img/test_image.png/new_name.png")
    assert response.status_code == 200
    assert response.json()["msg"] == "File updated successfully"
    # non-existent image
    response = client.put("/img/non_existent_image.png/new_name.png")
    assert response.status_code == 404
    assert response.json() == {"detail": "File not found"}

def test_delete_image():
    # existing image
    response = client.delete("/img/new_name.png")
    assert response.status_code == 200
    assert response.json()["msg"] == "File deleted successfully"
    # non-existent image
    response = client.delete("/img/non_existent_image.png")
    assert response.status_code == 404
    assert response.json() == {"detail": "File not found"}