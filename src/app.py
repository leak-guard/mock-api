from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api import config, water, probe, block, criteria

app = FastAPI()
app.include_router(config.router)
app.include_router(water.router)
app.include_router(probe.router)
app.include_router(block.router)
app.include_router(criteria.router)

@app.get("/hello")
async def hello():
    return JSONResponse({"text":"Hello World!"})


@app.get("/me")
async def me():

    return JSONResponse({"id":"this-is-my-id","mac":"this-is-my-mac-address"})
