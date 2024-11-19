from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response

import random

router = APIRouter(prefix="/water-block")

@router.get("")
async def get_water_block():
    return JSONResponse({"block": "active" if random.random() > 0.5 else "inactive"})

@router.post("")
async def post_water_block():
    return Response(status=status.HTTP_200_OK)

@router.get("/schedule")
async def get_water_block_schedule():
    pass    # TODO

@router.post("/schedule")
async def post_water_block_schedule():
    pass    # TODO
