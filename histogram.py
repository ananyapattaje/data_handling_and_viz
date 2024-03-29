import matplotlib.pyplot as plt
import numpy as np

# Use numpy to generate a bunch of random data in a bell curve around 5.
n = 5 + np.random.randn(1000)

m = [m for m in range(len(n))]
plt.bar(m, n)
plt.title("RAW DATA")
plt.show()

plt.hist(n, bins=10)
plt.title("HISTOGRAM")
plt.show()

plt.hist(n, cumulative=True, bins=20)
plt.title("CUMULATIVE HISTOGRAM")
plt.show()
