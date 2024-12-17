import psutil
import time
import os
import threading

shutdown_timer = None

def check_power_status():
    battery = psutil.sensors_battery()
    
    if battery is None:
        return None
    
    return battery.power_plugged

def shutdown_pc():
    os.system("shutdown now")

def reset_shutdown_timer():
    global shutdown_timer
    if shutdown_timer is not None:
        shutdown_timer.cancel()
    
    shutdown_timer = threading.Timer(20, shutdown_pc)
    shutdown_timer.start()

def main():
    last_plugged_in = True
    
    while True:
        plugged_in = check_power_status()
        
        if plugged_in is False and last_plugged_in:
            last_plugged_in = False
            print("Charger unplugged. Shutting down in 20 seconds...")
            reset_shutdown_timer()
        
        elif plugged_in is True:
            if last_plugged_in is False:
                print("Charger plugged back in. Cancelling shutdown.")
                last_plugged_in = True
                if shutdown_timer is not None:
                    shutdown_timer.cancel()
        
        time.sleep(1)

if __name__ == "__main__":
    main()
