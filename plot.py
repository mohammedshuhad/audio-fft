import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read data from the text file
real_parts = []
imag_parts = []
line_count = 0

with open('4KHz_dft.txt', 'r') as file:
    for line in file:
        line_count += 1
        # Remove parentheses and split by comma
        line = line.strip().strip('()')
        real, imag = map(float, line.split(','))
        real_parts.append(real)
        imag_parts.append(imag)

N = line_count - 1

# Step 2: Compute the magnitude
real_parts = [real / N for real in real_parts]
if real_parts:
    real_parts[0] /= 2
    real_parts[-1] /= 2

imag_parts = [imag / N for imag in imag_parts]
if imag_parts:
    imag_parts[0] /= 2
    imag_parts[-1] /= 2

mag_parts = [np.sqrt(real**2 + imag**2) for real, imag in zip(real_parts, imag_parts)]

# Step 3: Compute the phase
phase_parts = [np.arctan2(imag, real) for real, imag in zip(real_parts, imag_parts)]

# Step 4: Create x-axis values divided by 64
x_values = [((i / (N * 2)) * 20000) for i in range(len(mag_parts))]

# Step 5: Plot the real, imaginary, magnitude, and phase parts
plt.figure(figsize=(12, 24))

# Plot real parts
plt.subplot(4, 1, 1)
plt.plot(x_values, real_parts, label='Real Part', color='blue')
plt.title('Real Part of the Signal')
plt.xlabel('Sample Index (Divided by 64)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot imaginary parts
plt.subplot(4, 1, 2)
plt.plot(x_values, imag_parts, label='Imaginary Part', color='red')
plt.title('Imaginary Part of the Signal')
plt.xlabel('Sample Index (Divided by 64)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot magnitude parts
plt.subplot(4, 1, 3)
plt.plot(x_values, mag_parts, label='Magnitude Part', color='green')
plt.title('Magnitude of the Signal')
plt.xlabel('Sample Index (Divided by 64)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)

# Plot phase parts
plt.subplot(4, 1, 4)
plt.plot(x_values, phase_parts, label='Phase Part', color='purple')
plt.title('Phase of the Signal')
plt.xlabel('Sample Index (Divided by 64)')
plt.ylabel('Phase (radians)')
plt.legend()
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()