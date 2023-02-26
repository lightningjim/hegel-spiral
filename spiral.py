import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Hegel's path of Thought in his immanent critique
logic_array = ["Pure Being", "Pure Nothing", "Becoming", "Developing", "Determinate Being", "Negation & Reality", "Something", "Other", "Something and Other", "X", "Y"]
if(not(len(logic_array) % 2 == 1)):
	print("Array needs odd number of items")
	exit()

num_turns = int(len(logic_array)/2 - 1)
radius = 1
pitch = 1.5

num_half_turns = num_turns * 2
t = np.linspace(0, num_half_turns * np.pi, 2*num_half_turns+1)
x = radius * np.cos(t)
y = radius * np.sin(t)
z = pitch * t


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='Thought\'s path')

# add text labels
for i, txt in enumerate(np.arange(0, num_half_turns+1, 0.5)):
    if i % 2 == 0: # only label every other half turn
        ax.text(x[i], y[i], z[i], logic_array[int(i / 2)], color='red')

ax.legend()
plt.show()