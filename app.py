from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from musicgen import generate_music  # Assuming generate_music is a function in musicgen.py
from fastapi.responses import FileResponse
import os
import uvicorn
app = FastAPI()

class MusicRequest(BaseModel):
    description: List[str]
    duration: int = 8  # in seconds

@app.post("/generate")
def create_music(request: MusicRequest):
    try:
        wav_path = generate_music(request.description, request.duration)
        return FileResponse(wav_path, media_type="audio/wav", filename=os.path.basename(wav_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)