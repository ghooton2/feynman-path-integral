import matplotlib.pyplot as plt
import numpy as np
from scipy import random


a = -5
b = 5
N = 10
x_values = np.arange(0,4.1,0.5)
line_y = np.arange(-6,6,1.4)
print(line_y)
print(x_values)
plt.figure(figsize=(4,3))
for y in range(0, len(x_values)):
    lines = [x_values[y]]*len(x_values)
    plt.plot(lines, line_y, color='black', linestyle = '--')


for x in range(0,4):
    #x_values = x*0.2
    y_values = random.uniform(-5,5,9)
    print(y_values)
    y_values[0] = 0
    y_values[-1] = 0
    #y_values = [round(num) for num in y_values]
    plt.plot(x_values, y_values, label = 'Path ' + str(x))

plt.ylim([-5.5,5.5])

#plt.legend(loc='upper right')
plt.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0)
plt.xlabel('t')
plt.ylabel('x')
plt.show()

print(y_values)
