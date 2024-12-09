from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

import random
from typing import Literal

router = APIRouter(prefix="/probe")


class ProbeCommand(BaseModel):
    verb: Literal["block", "unblock"]

def get_probe_id(i):
    ids = [
        [
      3884552546,
      529462413,
      3488854973
    ],
    [
      3085004862,
      47908013,
      1135143305
    ],
    [
      591958241,
      4063424510,
      2265439981
    ],
    ]

    return ids[i]


def get_probe_info(i):
    return {
        "id": get_probe_id(i),
        "battery_level": random.randint(0, 100),
        "is_alarmed": random.random() > 0.9
    }

@router.get("")
async def get_probes():
    probe_ids = random.sample(range(256), 3)

    return JSONResponse({f"{probe_ids[i]}": get_probe_info(i) for i in range(3)})

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
async def get_pairing_status():
    return JSONResponse({"pairing": random.choice([True, False])})
