from fastapi import APIRouter
from starlette.responses import JSONResponse


router = APIRouter()


@router.get("/", tags=["meta"])
async def root():
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "message": "API RESTTT   is ready",
            "data": {
                "owner": "Oscar Cely",
                "source": "https://github.com/Oscarce10/photogram-backend"
            }
        }
    )
