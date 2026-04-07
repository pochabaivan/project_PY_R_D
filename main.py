import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router import router

# Inicializácia FastAPI aplikácie
app = FastAPI(
    title="Weather Comparison Tool",
    description="Aplikácia na porovnávanie agrometeorologických metrík medzi mestami.",
    version="1.0.0"
)

# Pripojenie routera s prefixom (voliteľné) alebo priamo na root
app.include_router(router)

# Spustenie servera (vhodné pre vývoj)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
