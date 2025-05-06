def carPooling(trips: List[List[int]], capacity: int) -> bool:
    timestamp = []
    for trip in trips:
        timestamp.append((trip[1], trip[0]))  # (start, passengers)
        timestamp.append((trip[2], -trip[0])) # (end, -passengers)
    
    timestamp.sort()  # Sort by location
    
    current_passengers = 0
    for time, passenger_change in timestamp:
        current_passengers += passenger_change
        if current_passengers > capacity:
            return False
    
    return True