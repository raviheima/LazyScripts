# ChargeSense

This is a simple Python script I wrote to automatically shut down my PC when unplugged from the charger, particularly useful during idle activities like listening to music. The script helps conserve battery for later use, and it can also prevent guests (like friends) from using the PC when it's on battery power.

## Features

- **Automatic Shutdown:** When the charger is unplugged, the PC will shut down after 20 seconds of idle time.
- **Shutdown Timer Reset:** If the charger is plugged back in within the 20-second countdown, the shutdown is canceled.
- **Customizable:** Feel free to tweak the script as you like to better suit your needs.

## How It Works

1. It checks the battery status to see if the charger is plugged in.
2. If unplugged, it starts a 20-second countdown to shut down the system.
3. If plugged back in within the countdown window, the shutdown is canceled and the timer resets.

## Requirements

- Python 3.x
- `psutil` library (install with `pip install psutil`)

## Tested On

- Linux Debian

## Usage

Simply run the script, and it will handle the rest. Make sure to have Python and the required library installed.

```bash
python chargesense.py
```

Enjoy! :)