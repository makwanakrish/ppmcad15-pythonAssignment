# This script monitors the CPU usage of your computer.
# If the usage is too high (over 80%), it shows an alert.

import psutil
import time
import os

# Set the maximum usage allowed before an alert is shown.
THRESHOLD_PERCENT = 80

def monitor_cpu_health():
    """
    Continuously monitors the CPU usage and prints an alert if it is too high.
    """
    print("--- Starting CPU Monitor ---")
    print(f"Monitoring CPU usage. Alert threshold is set to {THRESHOLD_PERCENT}%")

    # This loop runs forever until you stop the script (by pressing Ctrl+C).
    while True:
        try:
            # Get the current CPU usage as a percentage.
            # interval=None means it returns the value right now.
            cpu_usage = psutil.cpu_percent(interval=1)

            # Check if the usage is higher than our limit (threshold).
            if cpu_usage > THRESHOLD_PERCENT:
                # If it is high, print an ALER T.
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                # If it is low, just print the current status (optional)
                # print(f"Current CPU usage is normal: {cpu_usage}%")
                pass

            # Wait for 3 seconds before checking the CPU again.
            time.sleep(3)

        except Exception as e:
            # If something goes wrong (error handling), print a message and stop.
            print(f"An error happened during monitoring: {e}")
            break

# We start the monitor when the script is run.
if __name__ == "__main__":
    # Check if psutil is available before starting
    try:
        # Check if the required function exists
        if hasattr(psutil, 'cpu_percent'):
            monitor_cpu_health()
        else:
            print("Error: psutil is installed, but the cpu_percent function is missing or not working.")
    except ImportError:
        print("Error: The 'psutil' library is not installed.")
        print("Please install it using your terminal: pip install psutil")
    except KeyboardInterrupt:
        # This handles when the user presses Ctrl+C to stop the script.
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")