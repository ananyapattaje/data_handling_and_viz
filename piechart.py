import matplotlib.pyplot as plt

labels = 'A', 'B', 'C'
sections = [56, 66, 24]
colors = ['c', 'r', 'y']

plt.pie(sections, labels=labels, colors=colors,
        startangle=100,
        explode = (0, 0.1, 0),
        autopct = '%1.2f%%')

plt.axis('equal') # Try commenting this out.
plt.title('PIE CHART EXAMPLE')
plt.show()
