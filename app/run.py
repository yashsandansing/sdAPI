from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from bark import generate_audio, SAMPLE_RATE
from scipy.io.wavfile import write as write_wav
from fastapi.responses import FileResponse
import tempfile
import os

app = FastAPI()

class Item(BaseModel):
    text_prompt: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/text2speech/")
async def text2speech(item: Item, background_tasks: BackgroundTasks):
    if item.text_prompt:
        try:
            audio_array = generate_audio(item.text_prompt)            
            temp = tempfile.mktemp('.wav')
            write_wav(temp, SAMPLE_RATE, audio_array)
            background_tasks.add_task(os.remove, path=temp)
            headers = {'Content-Disposition': f'attachment; filename="{temp}"'}
            return FileResponse(f'{temp}',headers=headers, media_type="audio/wav")
        except:
            return "An error occured"
    else:
        "Invalid Text prompt"