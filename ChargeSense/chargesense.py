import psutil
import time
import os

def check_power_status():
    # Get battery information
    battery = psutil.sensors_battery()
    
    if battery is None:
        return None
    
    # Check if the laptop is plugged in (charging)
    plugged = battery.power_plugged
    return plugged

def shutdown_pc():
    print("Unplugged from charger. Shutting down in 30 seconds...")
    time.sleep(30)  # Wait for 30 seconds before shutting down
    os.system("shutdown now")  # Shut down the system

def main():
    last_plugged_in = True
    
    while True:
        plugged_in = check_power_status()
        
        # If the laptop was plugged in and now it's unplugged
        if plugged_in is False and last_plugged_in:
            last_plugged_in = False
            shutdown_pc()
        
        # If it's plugged back in, reset the state
        elif plugged_in is True:
            last_plugged_in = True
        
        # Sleep for a short period before checking again
        time.sleep(1)

if __name__ == "__main__":
    main()
