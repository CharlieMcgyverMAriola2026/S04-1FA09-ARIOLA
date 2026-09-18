import math

def get_distance():
    print("1. Lat/Lon (km)\n2. 2D Points (X/Y)")
    choice = input("Choice (1 or 2): ")

    if choice == "1":
        lat1, lon1 = float(input("Lat 1: ")), float(input("Lon 1: "))
        lat2, lon2 = float(input("Lat 2: ")), float(input("Lon 2: "))
        
        # Haversine formula
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        km = 6371 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        print(f"Distance: {km:.2f} km")

    elif choice == "2":
        x1, y1 = float(input("X1: ")), float(input("Y1: "))
        x2, y2 = float(input("X2: ")), float(input("Y2: "))
        
        dist = math.hypot(x2 - x1, y2 - y1)
        print(f"Distance: {dist:.2f} units")

if __name__ == "__main__":
    get_distance()
