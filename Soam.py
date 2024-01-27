import time
import threading
import keyboard  # Import the keyboard library for detecting key presses

# Function to simulate pressing the spacebar
def press_spacebar():
    keyboard.press_and_release('space')

# Function to check for kill switch
def check_kill_switch():
    global kill_switch_pressed
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('f'):
            kill_switch_pressed = True
            break

# Main loop
kill_switch_pressed = False
kill_switch_thread = threading.Thread(target=check_kill_switch)
kill_switch_thread.start()

while not kill_switch_pressed:
    try:
        press_spacebar()  # Simulate pressing spacebar
        time.sleep(300)  # Wait for 5 minutes (300 seconds)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break

# Wait for the kill switch thread to finish
kill_switch_thread.join()
