'''
Question 10: GPS Location Tracking
A delivery application stores the latitude and longitude of a delivery location in a tuple. Write a function to display the coordinates and 
determine whether they represent a location in the approximate bounding box of Kolkata: latitude 22.4–22.8 and longitude 88.2–88.5.

'''

def check_kolkata_location(location):
    latitude, longitude = location
    print(f"Coordinates: \n Latitude {latitude} \n Longitude {longitude}")
    in_kolkata = (
        22.4 <= latitude <= 22.8
        and 88.2 <= longitude <= 88.5
    )
    match in_kolkata:
        case True:
            print("The location is inside the approximate Kolkata bounding box.")
        case False:
            print("The location is outside the approximate Kolkata bounding box.")

check_kolkata_location((22.5726, 88.3639))
print()



