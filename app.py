from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

# Serve static files (pygbag build output)
app.mount("/static", StaticFiles(directory="build/web", html=True), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/")