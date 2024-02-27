#!/bin/bash

# Function to simulate pressing the spacebar
press_spacebar() {
    xdotool key space
}

    press_spacebar  # Simulate pressing spacebar
    sleep 300       # Wait for 5 minutes
done &

# Cleanup
wait
