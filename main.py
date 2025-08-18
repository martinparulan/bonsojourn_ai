import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

load_dotenv()

APP_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.join(APP_DIR, "bon_sojourn")
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080", "*"]
SERVE_WEB_INTERFACE = True

app: FastAPI = get_fast_api_app(
    agents_dir=AGENTS_DIR,
    allow_origins=ALLOWED_ORIGINS,
    web=SERVE_WEB_INTERFACE,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
