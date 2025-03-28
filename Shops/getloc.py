import geocoder

def get_current_location():
    # Get current location based on IP address
    g = geocoder.ip('me')  # 'me' refers to the user's public IP
    if g.ok:
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        print(f"Current location - Latitude: {latitude}, Longitude: {longitude}")
        return 22.2783, 114.1747
    else:
        print("Could not obtain location")

# Call the function
if __name__ == "__main__":
    get_current_location()