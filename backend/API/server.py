from fastapi import FastAPI

import APIRequests.startup as startup

app = FastAPI()

app.include_router(startup.router)
