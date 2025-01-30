from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class ResponseModel(BaseModel):
    email: str
    current_datetime: str
    github_url: str

@app.get("/", response_model=ResponseModel)
def get_info():
    return {
        "email": "ericangeloawa@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/yourusername/your-repo"
    }
