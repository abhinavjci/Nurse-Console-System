import csv
import random
import time
# import winsound

def roomCodeLoader(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def run_simulation(roomCodes):
    emergency_codes = ['Code  Blue', 'Code White']
    print("Started....\n")
    
    try:
        while True:
            wait_time = random.randint(10, 30)  # 1 to 2 minutes
            time.sleep(wait_time)

            code = random.choice(emergency_codes)
            location = random.choice(roomCodes)
            # winsound.Beep(1000, 1000)

            print(f"> {code} | {location}")
    except KeyboardInterrupt:
        print("\nSimulation stopped manually.")

# Run the program
if __name__ == "__main__":
    roomCodes = roomCodeLoader("Codes.csv")
    run_simulation(roomCodes)
