# 指定使用的鏡像
FROM python:3.12.4-alpine

# 設定工作資料夾
WORKDIR /app

# 複製當前位置檔案到工作資料夾
COPY . /app

# 安裝必要套件
RUN pip install fastapi uvicorn

# 指定埠號
EXPOSE 8000

# 啟動uvicorn伺服, 指定主應用, 設定開放的host與port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 