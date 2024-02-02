import matplotlib.pyplot as plt

# voltage and current for mystery resistor
voltage = [-10, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 10]
current = [-1.483, -0.222, -0.149, -0.075, 0, 0.075, 0.149, 0.222, 1.483]

# Plotting the relationship between voltage and current
plt.figure(figsize=(10, 6))
plt.plot(voltage, current, marker='o', linestyle='-', color='blue')
plt.title('Resistor Voltage vs Current')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.grid(True)

# Display the plot
plt.show()