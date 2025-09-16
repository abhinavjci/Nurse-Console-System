import csv
import random
import time
# import winsound  # Windows-only

# Load room codes from CSV
def load_room_codes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

# Main simulation loop
def run_simulation(room_codes):
    emergency_codes = ['Code Red', 'Code Blue', 'Code White']
    print("🚨 Hospital Code Simulator Started. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            wait_time = random.randint(10, 30)  # 1 to 2 minutes
            time.sleep(wait_time)

            code = random.choice(emergency_codes)
            location = random.choice(room_codes)

            # Beep: frequency=1000Hz, duration=1000ms
            # winsound.Beep(1000, 1000)

            print(f"🔊 {code} announced at location {location}")
    except KeyboardInterrupt:
        print("\nSimulation stopped manually.")

# Run the program
if __name__ == "__main__":
    room_codes = load_room_codes("Codes.csv")
    run_simulation(room_codes)
