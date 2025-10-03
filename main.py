import csv
import random
import time
# import winsound  # For sound alerts on Windows
import os        # Optional: for cross-platform checks

def roomCodeLoader(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def get_color(code):
    code = code.lower()
    if "red" in code:
        return "\033[91m"  # Red
    elif "blue" in code:
        return "\033[94m"  # Blue
    elif "white" in code:
        return "\033[97m"  # White
    elif "pink" in code:
        return "\033[95m"  # Pink
    else: 
        return "\033[0m"   # Default

def run_simulation(roomCodes):
    emergency_codes = ['Code Blue ', 'Code White', 'Code Pink ', 'Code Red  ']
    print("Started....\n")
    
    try:
        while True:
            wait_time = random.randint(15, 15)
            time.sleep(wait_time)

            code = random.choice(emergency_codes)
            location = random.choice(roomCodes)
            color = get_color(code)

            # Sound alert (Windows only)
            # winsound.Beep(1000, 1000)

            print(f"{color}‖\033[0m {code} | {location}")  # Reset color
    except KeyboardInterrupt:
        print("\nSimulation stopped manually.")

# Run the program
if __name__ == "__main__":
    roomCodes = roomCodeLoader("Codes.csv")
    run_simulation(roomCodes)