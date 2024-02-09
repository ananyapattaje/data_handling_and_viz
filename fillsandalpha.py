import matplotlib.pyplot as plt
import numpy as np

ys = 100 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 95, where=(ys > 95), facecolor='c', alpha=0.6)

plt.title("FILLS AND ALPHA")
plt.show()
