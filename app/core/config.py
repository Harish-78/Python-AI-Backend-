import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")
EMBEDDING_MODEL = "text-embedding-3-small"
MAX_PDF_SIZE_MB = 20
DOWNLOAD_TIMEOUT_SECONDS = 30