from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Budget Brain API")

# Allow mobile + web apps to connect during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later we’ll restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "message": "Budget Brain backend is alive"}
