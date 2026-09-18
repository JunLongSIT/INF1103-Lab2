import time

print("--- Traffic Light Simulation Starting (10 Seconds) ---")

# Track the total simulation time
start_time = time.time()
duration = 10  # seconds

# Initial light state
light_state = "Green"

while time.time() - start_time < duration:
    # 1. Print the action based on the current light state
    if light_state == "Green":
        print("Light is Green -> Go")
        time.sleep(2)  # Keep the green light active for 2 seconds
        light_state = "Yellow"  # Transition to next state
        
    elif light_state == "Yellow":
        print("Light is Yellow -> Slow Down")
        time.sleep(1)  # Keep the yellow light active for 1 second
        light_state = "Red"  # Transition to next state
        
    elif light_state == "Red":
        print("Light is Red -> Stop")
        time.sleep(2)  # Keep the red light active for 2 seconds
        light_state = "Green"  # Cycle back to Green

print("--- Traffic Light Simulation Finished ---")
