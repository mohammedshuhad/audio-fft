import matplotlib.pyplot as plt

# Step 1: Read samples from the text file
samples = []
with open('1KHz.txt', 'r') as file:
    for line in file:
        samples.append(float(line.strip()))

# Step 2: Plot the samples
plt.plot(samples)
plt.title('Sample Plot')
plt.xlabel('Sample Index')
plt.ylabel('Sample Value')
plt.grid(True)
plt.show()