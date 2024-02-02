import matplotlib.pyplot as plt

# voltage and current for diode
voltage = [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5]
current = [0, 0, 0, 0, 0, 0, 0, 0, 0.015, 11.98, 37.75]

# Plotting the relationship between voltage and current
plt.figure(figsize=(10, 6))
plt.plot(voltage, current,color='red')
plt.title('Red Diode Voltage vs Current')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.grid(True)

# Display the plot
plt.show()