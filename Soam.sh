#!/bin/bash

# Function to simulate pressing the spacebar
press_spacebar() {
    xdotool key space
}

# Main loop
kill_switch_pressed=false
while [ "$kill_switch_pressed" != true ]; do
    press_spacebar  # Simulate pressing spacebar
    sleep 300       # Wait for 5 minutes
done &

# Check for kill switch (Ctrl+Alt+F)
trap 'kill $!' INT
while :
do
    read -n1 key
    if [ "$key" == $'\x06' ]; then  # Check for Ctrl+Alt+F (ASCII values: Ctrl=^, Alt=Alt, F=F)
        kill_switch_pressed=true
        break
    fi
done

# Cleanup
wait
