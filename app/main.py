from datetime import date
from fastapi import FastAPI,Query,Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/home")
def get_home():
    return{
        "Hello World"
    }



class HotelSearchArgs:
    def __init__(
            self,
            location: int,
            date_from: date,
            date_to: date,
            stars: Optional[int] = Query(None, ge=1,le=5),
            has_spa: Optional[bool] = None
            ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa
        

class Sbooking (BaseModel):
    room_id: int
    date_to: date
    date_from: date

class Shotel (BaseModel):
    address:str
    name:str
    stars: int




@app.get("/hotels")
def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    hotels = [
        {
            "address": "rfghrgbrg",
            "name": "rtgrtfgtr",
            "stars": 5, 
        }
    ]
    return hotels

@app.post("/bookings")
def bookings(booking: Sbooking):
    pass

