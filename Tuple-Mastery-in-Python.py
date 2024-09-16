# Task 1: Formatting Flight Itineraries:
def format_itineraries(flight_list):
    result = ""
    for i, (traveler_name, origin, destination) in enumerate(flight_list, 1):
        result += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return result

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(flights)
print(formatted_itineraries)