from datetime import datetime

from fastapi import APIRouter, Depends

from weather.schemas import CityParams, CityResponse
from weather.service import get_city_suggestion


weather_router = APIRouter(prefix = "")

@weather_router.get(path = "/citysuggest", status_code = 200)#, response_model = CityResponse)
async def city_suggestion(params: CityParams = Depends()):
    params = params.model_dump()
       
    response = get_city_suggestion(params["startmonth"], params["endmonth"])
    
    return response
    