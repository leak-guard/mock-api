from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

import random
from typing import Literal

router = APIRouter(prefix="/probe")


class ProbeCommand(BaseModel):
    verb: Literal["block", "unblock"]

def get_probe_id():
    return [random.randint(0, 4294967295) for _ in range(3)]

def get_probe_info():
    return {
        "id": get_probe_id(),
        "battery_level": random.randint(0, 100),
        "blocked": random.random() > 0.9
    }

@router.get("")
async def get_probes():
    probe_count = random.randint(0, 10)
    probe_ids = random.sample(range(256), probe_count)

    return JSONResponse({f"{probe_ids[i]}": get_probe_info() for i in range(probe_count)})

@router.get("/id/{id}")
async def get_probe(id: int):
    return JSONResponse(get_probe_info())

@router.put("/id/{id}")
async def put_probe(id: int, command: ProbeCommand):
    return Response(status_code=status.HTTP_200_OK)

@router.delete("/id/{id}")
async def delete_probe(id: int):
    return Response(status_code=status.HTTP_200_OK)

@router.post("/pair/enter")
async def enter_pairing_mode():
    return Response(status_code=status.HTTP_200_OK)

@router.post("/pair/exit")
async def exit_pairing_mode():
    return Response(status_code=status.HTTP_200_OK)

@router.get("/pair")
async def get_probes_to_pair():
    return JSONResponse({"probes": [get_probe_id() for _ in range(random.randint(0, 10))]})
