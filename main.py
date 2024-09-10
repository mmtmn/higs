import time
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
initial_temp = 1e12  # Starting temperature in Kelvin (hot universe)
expansion_rate = 0.1  # Expansion rate of the universe
cooling_rate = 0.9  # Cooling rate during expansion
higgs_field_strength = 0  # Initially, Higgs field is switched off
resonant_frequency_increase = []  # Track resonant frequency increase due to Higgs field

# Story narration
story = """
Once upon a time, there came into being a universe. Searingly hot, it swarmed with elementary particles. 
Among its fields was a Higgs field, initially switched off. But as the universe expanded and cooled, 
the Higgs field suddenly switched on, developing a nonzero strength. When this happened, many fields became stiff, 
and as a result, their particles acquired resonant frequencies and mass. That’s how the universe was transformed, 
through the influence of the Higgs field, into the quantum musical instrument it is today.

In truth, the Higgs field doesn't slow particles down or act like molasses; instead, it’s a cosmic stiffening agent. 
It causes fields like the electron field to resonate, increasing the frequency of their vibrations, which gives their particles mass. 
In the universe, mass is a direct result of this resonance, much like the way a guitar string vibrates at a specific frequency.
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

        # Resonant frequency increases as Higgs field strengthens
        frequency_increase = np.log(1 + higgs_field_strength * 10)  # Non-linear relation between Higgs and frequency
        resonant_frequency_increase.append(frequency_increase)

        temperatures.append(temp)
        higgs_field_strengths.append(higgs_field_strength)

        # Print the status every few steps
        if time_step % 10 == 0:
            print(f"Time step {time_step}: Temperature = {temp:.2e} K, Higgs field strength = {higgs_field_strength:.2f}, "
                  f"Resonant frequency increase = {frequency_increase:.2f}")

        time_step += 1
        time.sleep(0.2)

    return temperatures, higgs_field_strengths, resonant_frequency_increase

# Run the universe expansion simulation
temperatures, higgs_field_strengths, resonant_frequencies = simulate_universe_expansion()

# Plotting the result
plt.figure(figsize=(10, 6))

# Plot temperature over time
plt.plot(temperatures, label="Temperature (K)", color="red")
plt.plot(higgs_field_strengths, label="Higgs Field Strength", color="blue")
plt.plot(resonant_frequencies, label="Resonant Frequency Increase", color="green")
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.title('Universe Cooling, Higgs Field Activation, and Resonant Frequency Increase')
plt.legend()

# Save the plot to a file instead of showing it
plt.savefig("universe_simulation_plot.png")

print("Plot saved as 'universe_simulation_plot.png'")
