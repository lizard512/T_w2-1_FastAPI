# FastAPI 圖片上傳與管理

這是一個使用 FastAPI 框架建立、用於圖片上傳和管理的簡易後端程式，作為學習目的的測試專案。
另包含了Docker compose流程的一些文檔，作為過程紀錄，故保留相關檔案。

## 功能

- **create_upload_image**: 允許使用者上傳圖片。
- **get_image**: 通過檔案名稱獲取圖片。
- **list_uploaded_images**: 列出所有已上傳的圖片及其檔名、檔案大小等資訊。
- **update_image**: 允許使用者修改已上傳的圖片名稱。
- **delete_image**: 允許使用者刪除已上傳的圖片。

## How to start

### install FastAPI
\`pip install fastapi uvicorn\`

### run the server
\`uvicorn main:app --reload\`
or
\`fastapi dev main.py\`

若成功完成操作，會在 \`http://127.0.0.1:8000\` 啟動伺服器。
可訪問 \`http://127.0.0.1:8000/docs\` 查看 API 文檔並進行測試。