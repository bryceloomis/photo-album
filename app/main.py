from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="Photo Album")

# Set up paths
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
PHOTOS_DIR = STATIC_DIR / "photos"

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)


def get_photos() -> list[dict]:
    """Get list of photos from the photos directory."""
    photos = []
    if PHOTOS_DIR.exists():
        for photo_path in sorted(PHOTOS_DIR.iterdir()):
            if photo_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
                photos.append({
                    "filename": photo_path.name,
                    "url": f"/static/photos/{photo_path.name}",
                })
    return photos


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page - displays the photo gallery."""
    photos = get_photos()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "photos": photos}
    )


@app.get("/health")
async def health():
    """Health check endpoint for DigitalOcean."""
    return {"status": "ok"}
