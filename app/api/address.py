from fastapi import APIRouter, HTTPException, Query
from typing import List
from geopy.distance import geodesic
from api.schemas import Address
from db.database import conn
from utils.validation import validate_address  
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Initialize APIRouterm
router = APIRouter()

@router.post("/addresses/", response_model=Address)
async def create_address(address: Address):
    """Create a new address."""
    try:
        validate_address(address)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO addresses (street, city, state, country, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)",
                  (address.street, address.city, address.state, address.country, address.latitude, address.longitude))
        address_id = c.lastrowid

    logger.info(f"Address created: {address_id}")
    return {"id": address_id, **address.dict()}

@router.put("/addresses/{address_id}", response_model=Address)
async def update_address(address_id: int, address: Address):
    """Update an existing address."""
    try:
        validate_address(address)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    with conn:
        c = conn.cursor()
        c.execute("UPDATE addresses SET street=?, city=?, state=?, country=?, latitude=?, longitude=? WHERE id=?",
                  (address.street, address.city, address.state, address.country, address.latitude, address.longitude, address_id))

    logger.info(f"Address updated: {address_id}")
    return {"id": address_id, **address.dict()}

@router.delete("/addresses/{address_id}")
async def delete_address(address_id: int):
    """Delete an address."""
    with conn:
        c = conn.cursor()
        c.execute("DELETE FROM addresses WHERE id=?", (address_id,))

    logger.info(f"Address deleted: {address_id}")
    return {"message": "Address deleted successfully"}

@router.get("/addresses/")
async def get_addresses_within_distance(latitude: float, longitude: float, distance: float = Query(..., gt=0)):
    """Get addresses within a specified distance from given coordinates."""
    addresses = []
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM addresses")
        rows = c.fetchall()
        for row in rows:
            addr_id, street, city, state, country, addr_lat, addr_long = row
            addr_coords = (addr_lat, addr_long)
            user_coords = (latitude, longitude)
            if geodesic(user_coords, addr_coords).kilometers <= distance:
                addresses.append({
                    "id": addr_id,
                    "street": street,
                    "city": city,
                    "state": state,
                    "country": country,
                    "latitude": addr_lat,
                    "longitude": addr_long
                })

    logger.info(f"Addresses within distance: {addresses}")
    return addresses
