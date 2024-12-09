from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

import random

router = APIRouter(prefix="/criteria")

@router.get("")
async def get_criteria():
    return JSONResponse({"criteria": "T,1,30,|"})

@router.post("")
async def post_criteria():
    return Response(status_code=status.HTTP_200_OK)
