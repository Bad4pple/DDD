from fastapi import FastAPI
from pydantic import BaseModel
import services

app = FastAPI()

class ResidentRequest(BaseModel):
    reference_room: str
    reference_customer: str
    fistname: str
    surname: str

@app.get("/{id}")
async def root(id: str):
    room = services.get_room(id)
    return room 

@app.post("/")
async def new_resident_in_room(entity: ResidentRequest):

    result = services.lease_system(
        reference_room=entity.reference_room,
        reference_customer=entity.reference_customer,
        firstname=entity.fistname,
        surname=entity.surname
    )

    if result == "error":
        return result

    return result
