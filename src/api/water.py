from fastapi import APIRouter
from fastapi.responses import JSONResponse

import random
import math
import time
import datetime

router = APIRouter(prefix="/water-usage")

def get_timestamped_usages(from_timestamp, to_timestamp):
    delta_secs = to_timestamp - from_timestamp
    
    # TODO: Support varying resolutions (more recent - more common)
    record_count = math.ceil(delta_secs / 60 + 0.01)
    usages = {(from_timestamp + i * 60): round(random.random() * 10, 2) for i in range(record_count)}
    
    return usages

@router.get("")
async def get_water_usage():
    return JSONResponse({
        "flow_rate": random.randint(1000,10000),
        "total_volume": random.randint(100000,1000000),
        "today_volume": random.randint(50000,700000)
    })

@router.get("/{from_timestamp}/{to_timestamp}")
async def get_water_usage_range(from_timestamp: int, to_timestamp: int):
    return JSONResponse({"usages": get_timestamped_usages(from_timestamp, to_timestamp)})

@router.get("/today")
async def get_water_usage_today():
    now = datetime.datetime.now()
    today_start = datetime.datetime(now.year, now.month, now.day)

    from_timestamp = int(time.mktime(today_start.timetuple()))
    to_timestamp = int(time.mktime(now.timetuple()))

    usages = get_timestamped_usages(from_timestamp, to_timestamp)

    return JSONResponse({"usages": usages})

    