from fastapi import FastAPI, File, UploadFile
import shutil
import os
from pathlib import Path



app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    img_path = Path("input.jpg")
    with open(img_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Run detection (assuming detect.py exists in yolov11/)
    os.system("python yolov11/detect.py --weights best.pt --source input.jpg --save-txt --conf 0.25")

    return {"message": "Prediction complete, check output"}
@app.get("/")
def read_root():
    return {"message": "YOLOv11 API is running. Use POST /predict/ to make predictions."}


