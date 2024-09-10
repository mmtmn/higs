import time
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
initial_temp = 1e12  # Starting temperature in Kelvin (hot universe)
cooling_rate = 0.9  # Cooling rate during expansion
higgs_field_strength = 0  # Initially, Higgs field is switched off
gravitational_strength = 0  # Gravitational force starts weak
electromagnetic_strength = 0  # Electromagnetic force starts weak
strong_force_strength = 0  # Strong nuclear force
weak_force_strength = 0  # Weak nuclear force

# Track resonant frequency increase and force strengths
resonant_frequency_increase = []
gravitational_forces = []
electromagnetic_forces = []
strong_forces = []
weak_forces = []

# Story narration
story = """
Once upon a time, there came into being a universe. Searingly hot, it swarmed with elementary particles.
At first, all forces were unified. As the universe expanded and cooled, these forces separated. 
Among its fields was a Higgs field, initially switched off. But as the universe cooled, the Higgs field suddenly switched on, 
developing a nonzero strength. This stiffened many fields, giving their particles resonant frequencies and mass.

As the universe cooled further, the four fundamental forces took shape: gravitational, electromagnetic, strong, and weak forces.
The gravitational force began to organize large structures. The strong nuclear force bound quarks into protons and neutrons,
while the weak force enabled nuclear fusion in the early universe. The electromagnetic force shaped atoms and molecules.

Together, these forces structured the universe, transforming it into the intricate cosmic symphony we see today.
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

        # Forces grow and separate as the universe cools
        gravitational_strength = np.log(1 + temp / initial_temp * 10)  # Gravitational force
        electromagnetic_strength = np.log(1 + temp / initial_temp * 5)  # Electromagnetic force
        strong_force_strength = np.log(1 + temp / initial_temp * 7)  # Strong nuclear force
        weak_force_strength = np.log(1 + temp / initial_temp * 4)  # Weak nuclear force

        gravitational_forces.append(gravitational_strength)
        electromagnetic_forces.append(electromagnetic_strength)
        strong_forces.append(strong_force_strength)
        weak_forces.append(weak_force_strength)

        temperatures.append(temp)
        higgs_field_strengths.append(higgs_field_strength)

        # Print the status every few steps
        if time_step % 10 == 0:
            print(f"Time step {time_step}: Temp = {temp:.2e} K, Higgs Field = {higgs_field_strength:.2f}, "
                  f"Gravitational = {gravitational_strength:.2f}, Electromagnetic = {electromagnetic_strength:.2f}, "
                  f"Strong = {strong_force_strength:.2f}, Weak = {weak_force_strength:.2f}, "
                  f"Resonant Frequency = {frequency_increase:.2f}")

        time_step += 1
        time.sleep(0.2)

    return temperatures, higgs_field_strengths, resonant_frequency_increase, gravitational_forces, electromagnetic_forces, strong_forces, weak_forces

# Run the universe expansion simulation
(temperatures, higgs_field_strengths, resonant_frequencies, gravitational_forces, electromagnetic_forces, 
 strong_forces, weak_forces) = simulate_universe_expansion()

# Plotting the results
plt.figure(figsize=(12, 8))

# Plot temperature over time
plt.plot(temperatures, label="Temperature (K)", color="red")
plt.plot(higgs_field_strengths, label="Higgs Field Strength", color="blue")
plt.plot(resonant_frequencies, label="Resonant Frequency Increase", color="green")
plt.plot(gravitational_forces, label="Gravitational Force", color="purple")
plt.plot(electromagnetic_forces, label="Electromagnetic Force", color="orange")
plt.plot(strong_forces, label="Strong Nuclear Force", color="brown")
plt.plot(weak_forces, label="Weak Nuclear Force", color="cyan")
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.title('Universe Cooling, Forces Activation, and Higgs Field Influence')
plt.legend()

# Save the plot to a file instead of showing it
plt.savefig("universe_forces_simulation_plot.png")

print("Plot saved as 'universe_forces_simulation_plot.png'")
