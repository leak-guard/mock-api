from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response

router = APIRouter(prefix="/config")

@router.get("")
async def get_config():
    return JSONResponse({
        "ssid": "TestNetwork",
        "passphrase": "hunter2",
        "flow_meter_impulses": 400,
        "valve_type": "no",
    })

@router.put("")
async def put_config():
    return Response(status_code=status.HTTP_200_OK)