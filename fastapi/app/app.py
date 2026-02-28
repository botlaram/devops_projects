import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

# Read Mongo URL from environment variable
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["userdb"]
collection = db["users"]

app = FastAPI()
Instrumentator().instrument(app).expose(app)
templates = Jinja2Templates(directory="templates")

# home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# create page
@app.get("/create", response_class=HTMLResponse)
def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/create")
def create_user(
    request: Request,
    username: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...)
):
    collection.insert_one({
        "username": username,
        "phone": phone,
        "city": city
    })
    return RedirectResponse("/", status_code=303)

# search page
@app.get("/search", response_class=HTMLResponse)
def search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
def search_user(request: Request, username: str = Form(...)):
    user = collection.find_one({"username": username})
    return templates.TemplateResponse(
        "search.html",
        {"request": request, "user": user}
    )

print("Routes loaded:", app.routes)
