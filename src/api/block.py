from typing import Dict, List
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

import random

class DaySchedule(BaseModel):
    enabled: bool
    hours: List[bool]

class Schedule(BaseModel):
    sunday: DaySchedule
    monday: DaySchedule
    tuesday: DaySchedule
    wednesday: DaySchedule
    thursday: DaySchedule
    friday: DaySchedule
    saturday: DaySchedule

def generate_random_day_schedule() -> DaySchedule:
    return DaySchedule(
        enabled=random.choice([True, False]),
        hours=[random.choice([True, False]) for _ in range(24)]
    )

router = APIRouter(prefix="/water-block")

@router.get("")
async def get_water_block():
    return JSONResponse({"block": "active" if random.random() > 0.5 else "inactive"})

@router.post("")
async def post_water_block():
    return Response(status_code=status.HTTP_200_OK)

@router.get("/schedule", response_model=Schedule)
async def get_water_block_schedule():
    return {
        "sunday": generate_random_day_schedule(),
        "monday": generate_random_day_schedule(),
        "tuesday": generate_random_day_schedule(),
        "wednesday": generate_random_day_schedule(),
        "thursday": generate_random_day_schedule(),
        "friday": generate_random_day_schedule(),
        "saturday": generate_random_day_schedule()
    }

@router.put("/schedule")
async def post_water_block_schedule():
    return Response(status_code=status.HTTP_200_OK)
