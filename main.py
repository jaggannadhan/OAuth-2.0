from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from routers.google import google_router
from routers.facebook import facebook_router
from routers.github import github_router
from routers.salesforce import salesforce_router
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include OAuth routers
app.include_router(google_router, prefix="/auth/google")
app.include_router(facebook_router, prefix="/auth/facebook")
app.include_router(github_router, prefix="/auth/github")
app.include_router(salesforce_router, prefix="/auth/salesforce")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})