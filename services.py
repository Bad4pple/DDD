import repository, models

def lease_system(reference_room: str, reference_customer,firstname: str, surname: str):
    repo = repository.RoomRepositoryMemory()

    room = repo.get(reference=reference_room)

    residents = [
        models.Resident(
            reference=reference_customer,
            firstname=firstname,
            surname=surname
        )
    ]

    if room.can_lease():
        room.lease(residents=residents)
        repo.save(room=room)
        return room
    
    else: 
        return "error"

def get_room(reference_id: str):
    repo = repository.RoomRepositoryMemory() 
    room = repo.get(reference=reference_id)

    return room