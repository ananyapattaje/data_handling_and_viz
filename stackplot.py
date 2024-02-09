import matplotlib.pyplot as plt

idxes = [ 1,  2,  3,  4,  5,  6,  7,  8,  9]
ar1  = [23, 40, 28, 43,  8, 44, 43, 18, 17]
ar2  = [17, 30, 22, 14, 17, 17, 29, 22, 30]
ar3  = [15, 31, 18, 22, 18, 19, 13, 32, 39]

# Adding legend for stack plots is tricky.
plt.plot([], [], color='y', label = 'D 1')
plt.plot([], [], color='c', label = 'D 2')
plt.plot([], [], color='g', label = 'D 3')

plt.stackplot(idxes, ar1, ar2, ar3, colors= ['y', 'c', 'g'])
plt.title('STACK PLOT EXAMPLE')
plt.legend()
plt.show()
