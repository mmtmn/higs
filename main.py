import time
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
initial_temp = 1e12  # Starting temperature in Kelvin (hot universe)
expansion_rate = 0.1  # Expansion rate of the universe
cooling_rate = 0.9  # Cooling rate during expansion
higgs_field_strength = 0  # Initially, Higgs field is switched off

# Story narration
story = """
Once upon a time, there came into being a universe. 
Searingly hot, it swarmed with elementary particles. 
Among its fields was a Higgs field, initially switched off.
But as the universe expanded and cooled, the Higgs field suddenly switched on, developing a nonzero strength.
When this happened, many fields became stiff, and as a result their particles acquired resonant frequencies and mass.
That’s how the universe was transformed, through the influence of the Higgs field, into the quantum musical instrument it is today.
"""

def simulate_universe_expansion():
    temp = initial_temp
    time_step = 0
    temperatures = []
    higgs_field_strengths = []

    print(story)
    time.sleep(2)

    while temp > 1e3:  # Stop when temperature is low enough
        temp *= cooling_rate  # Universe cools as it expands
        higgs_field_strength = max(1 - temp / initial_temp, 0)  # Higgs field grows as the universe cools

        temperatures.append(temp)
        higgs_field_strengths.append(higgs_field_strength)

        # Print the status every few steps
        if time_step % 10 == 0:
            print(f"Time step {time_step}: Temperature = {temp:.2e} K, Higgs field strength = {higgs_field_strength:.2f}")

        time_step += 1
        time.sleep(0.2)

    return temperatures, higgs_field_strengths

# Run the universe expansion simulation
temperatures, higgs_field_strengths = simulate_universe_expansion()

# Plotting the result
plt.figure(figsize=(10, 6))

# Plot temperature over time
plt.plot(temperatures, label="Temperature (K)", color="red")
plt.plot(higgs_field_strengths, label="Higgs Field Strength", color="blue")
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.title('Universe Cooling and Higgs Field Activation')
plt.legend()

# Display the plot
plt.show()
