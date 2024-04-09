from api.schemas import Address
def validate_address(address: Address):
    """Validate address coordinates."""
    if not (-90 <= address.latitude <= 90):
        raise ValueError("Latitude should be between -90 and 90")
    if not (-180 <= address.longitude <= 180):
        raise ValueError("Longitude should be between -180 and 180")
    

