import os
from dotenv import load_dotenv

# .env file se key load kar rahe hain
load_dotenv()

# Google API Key variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- RESUME OPTIMIZATION SETTINGS ---
# Hum chunk size 1000 rakh rahe hain. 
# Agar size chhota hoga to context toot jayega aur LLM hallucinations karega.
# Ye setting "40% reduced hallucinations" wale point ke liye zaroori hai.
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Models
EMBEDDING_MODEL = "models/embedding-001" # Google ka fast model
LLM_MODEL = "gemini-pro"

# Paths (Folders ke naam)
VECTOR_STORE_PATH = "data/vectorstore/faiss_index"
UPLOAD_DIR = "data/uploads"