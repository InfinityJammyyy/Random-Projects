import pyautogui
import time
import keyboard  

# This code was written by AI

# Function to press the spacebar
def press_spacebar():
    pyautogui.press('space')

# Main loop
kill_switch_pressed = False
while not kill_switch_pressed:
    try:
        press_spacebar()  # Press spacebar
        time.sleep(300)  # Wait for 5 minutes (300 seconds)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break
    # Check if Ctrl+Alt+F is pressed
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('f'):
        print("\nKill switch activated. Exiting program.")
        kill_switch_pressed = True
