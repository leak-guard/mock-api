from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

import random

router = APIRouter(prefix="/criteria")

@router.get("")
async def get_criteria():
    pass    # TODO

@router.get("/{id}")
async def get_criterion(id: int):
    pass    # TODO

@router.post("")
async def post_criteria():
    pass    # TODO
