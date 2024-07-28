from fastapi import Query

from pydantic import BaseModel

from typing import List, Optional


# Query parameters
class CityParams(BaseModel):
    startmonth: int
    endmonth: int
    
    def __init__(self,
                 startmonth: int = Query(
                     description = "start month"
                 ),
                 endmonth: int = Query(
                     description = "end month"
                 )):
        super().__init__(startmonth = startmonth,
                         endmonth = endmonth)
        self.startmonth = startmonth
        self.endmonth = endmonth
        

# Response model
class CityResponse(BaseModel):
    cities: Optional[List[str]] = None


class WeatherResponse(BaseModel):
    pass