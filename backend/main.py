from fastapi import FastAPI
from routers import user, job, application

app = FastAPI()

app.include_router(user.router)
app.include_router(job.router)
app.include_router(application.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Auto Job Apply API"}