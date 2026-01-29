import datetime

# Stations
ZONES = {
    "Central": ["Centrala", "Jaund", "Bylyn", "Rele", "Frestin", "Sath", "Ninia", "Tallan", "Lomil", "Yaen"],
    "Midtown": ["Riolva", "Quthiel", "Wicyt", "Agrafie", "Docia", "Stonyam", "Obelyn", "Ralith", "Garion", "Sylas", "Riladia", "Oloadus"],
    "Downtown": ["Erean", "Brunad", "Zord", "Marend", "Ryall", "Pryn", "Ederif", "Holmer", "Vertwall", "Ruril", "Pennad", "Kervia", "Elyot", "Adohad"]
}

# Fare in CENTS per zone [cite: 151, 153, 155, 157]
FARE_RATES = {
    "Adult": 2105,
    "Child": 1410,
    "Senior": 1025,
    "Student": 1750
}

def display_station_board():
    """Displays zones and an alphabetical list of stations in a table[cite: 142]."""
    print("\n" + "="*50)
    print(f"{'ZONE':<15} | {'STATIONS'}")
    print("-" * 50)
    for zone, stations in ZONES.items():
        sorted_stations = ", ".join(sorted(stations))
        print(f"{zone:<15} | {sorted_stations}")
    print("="*50 + "\n")

def get_valid_zone(prompt):
    """Validates zone selection[cite: 86, 143]."""
    zone_list = list(ZONES.keys())
    while True:
        print(f"{prompt}")
        for i, zone in enumerate(zone_list, 1):
            print(f"{i}. {zone}")
        try:
            choice = int(input("Select option: "))
            if 1 <= choice <= len(zone_list):
                return zone_list[choice - 1]
            print("Invalid choice. Please select a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_passenger_count(category):
    """Validates the number of passengers."""
    while True:
        try:
            count = int(input(f"Enter number of {category} travellers: "))
            if count >= 0:
                return count
            print("Number cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def issue_voucher():
    """Main logic for calculating fares and displaying the voucher [cite: 146-160]."""
    display_station_board()
    
    # 1. Select Zones
    start_zone = get_valid_zone("Select START zone:")
    dest_zone = get_valid_zone("Select DESTINATION zone:")
    
    # 2. Calculate Zones Travelled
    # Logic: 1 zone if same, 2 if adjacent (Central-Midtown), 3 if Downtown-Central [cite: 17]
    zone_order = {"Central": 0, "Midtown": 1, "Downtown": 2}
    zones_travelled = abs(zone_order[start_zone] - zone_order[dest_zone]) + 1
    
    # 3. Get Passenger Numbers
    passengers = {}
    for cat in FARE_RATES.keys():
        passengers[cat] = get_passenger_count(cat)
    
    total_passengers = sum(passengers.values())
    if total_passengers == 0:
        print("No passengers selected. Voucher cancelled.")
        return

    # 4. Display Voucher
    print("\n" + "*"*40)
    print("        CENTRALA TRANSPORT AUTHORITY")
    print(f"Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Route: {start_zone} to {dest_zone}")
    print(f"Zones Travelled: {zones_travelled}")
    print("-" * 40)
    
    grand_total = 0
    for cat, count in passengers.items():
        if count > 0:
            category_fare = FARE_RATES[cat] * zones_travelled
            category_total = category_fare * count
            grand_total += category_total
            print(f"{cat:<8} x{count:<2} | Fare: {category_fare}c | Subtotal: {category_total}c")
    
    print("-" * 40)
    print(f"TOTAL TRAVELLERS: {total_passengers}")
    print(f"GRAND TOTAL: {grand_total} CENTS")
    print("*"*40 + "\n")

def main():
    """Program entry point with restart option[cite: 161]."""
    while True:
        issue_voucher()
        again = input("Issue another voucher? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thank you for using CTA. Goodbye!")
            break

if __name__ == "__main__":
    main()