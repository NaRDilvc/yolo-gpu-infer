from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import shutil
import os

app = FastAPI()

model = YOLO("best.pt")

@app.post("/infer")
async def infer_image(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        results = model(temp_path)
        output = []

        for r in results:
            if hasattr(r, "probs") and r.probs is not None:
                output.append({
                    "class_id": int(r.probs.top1),
                    "confidence": float(r.probs.top1conf)
                })

        return {"results": output}

    finally:
        os.remove(temp_path)
