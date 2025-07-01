import psutil
import time
import os
import threading
import argparse

shutdown_timer = None

def check_power_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return None, None
    return battery.power_plugged, battery.percent

def shutdown_pc():
    os.system("systemctl suspend")
#    os.system("shutdown now")

def reset_shutdown_timer():
    global shutdown_timer
    if shutdown_timer is not None:
        shutdown_timer.cancel()
    shutdown_timer = threading.Timer(20, shutdown_pc)
    shutdown_timer.start()

def main(ignore_timer):
    last_plugged_in = True
    warning_issued = False  # Add a flag to avoid repeated warnings
    while True:
        plugged_in, percent = check_power_status()
        if plugged_in is False and last_plugged_in:
            last_plugged_in = False
            if not ignore_timer:
                print("Charger unplugged. Shutting down in 30 seconds...")
                reset_shutdown_timer()
        elif plugged_in is True:
            if last_plugged_in is False:
                print("Charger plugged back in. Cancelling shutdown.")
                last_plugged_in = True
                if shutdown_timer is not None:
                    shutdown_timer.cancel()
        # Issue warning if battery < 45% and not already warned
        if plugged_in is False and percent is not None and percent < 45 and not warning_issued:
            print(f"Warning: Battery at {percent}%. Please plug in your charger!")
            os.system("mpv /mnt/clover/Music/copyright-bg/Pixabay/upbeat-lo-fi-chill-instrumental-music-royalty-free-195449-liderc.mp3")
            warning_issued = True
        # Reset warning if battery goes above 45%
        if percent is not None and percent >= 45:
            warning_issued = False
        # Check battery percentage for shutdown
        if plugged_in is False and percent is not None and percent <= 40:
            print(f"Battery at {percent}%. Powering off immediately.")
            shutdown_pc()
            break
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ChargeSense battery monitor")
    parser.add_argument("--ignore-timer", action="store_true", help="Ignore shutdown timer when unplugged; only shutdown at 40% battery")
    args = parser.parse_args()
    main(args.ignore_timer)
