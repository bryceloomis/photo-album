# Photo Album

A simple photo gallery built with FastAPI and Jinja2 templates.

## Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Open http://localhost:8000 in your browser

## Adding Photos

Drop images into `app/static/photos/`. Supported formats: .jpg, .jpeg, .png, .gif, .webp

## Project Structure

```
photo-album/
├── app/
│   ├── main.py              # FastAPI application
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Styles
│   │   └── photos/          # Your images go here
│   └── templates/
│       ├── base.html        # Base template
│       └── index.html       # Gallery page
├── requirements.txt
└── README.md
```

## Deployment (DigitalOcean App Platform)

1. Push this repo to GitHub
2. Create a new App on DigitalOcean App Platform
3. Connect your GitHub repo
4. Set the run command to: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
