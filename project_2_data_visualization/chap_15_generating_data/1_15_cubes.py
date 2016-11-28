import matplotlib.pyplot as plt

x_values = list(range(1, 6))

y_values = [x**3 for x in x_values]


plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()


x_v = list(range(1, 1001))
y_v = [x**3 for x in x_v]


plt.scatter(x_v, y_v, c=y_v, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.show()

