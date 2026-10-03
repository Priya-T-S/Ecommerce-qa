from fastapi import FastAPI

app = FastAPI(
    title="E-Commerce QA Automation Platform",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }