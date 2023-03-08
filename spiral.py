import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Hegel's path of Thought in his immanent critique
being = ["Pure Being", "Becoming", "Determinate Being", "Something", "Change"]
nothing = ["Pure Nothing", "Stability", "Negation", "Other", "?"]
unity = ["?", "?", "?", "?", "?"]
explicit =  ["Ceasing", "Stablizing", "?", "?", "?"]
negation =  ["Arising", "Destabllizing", "?", "?", "?"]

# # Because of how each conecpt of being goes through it's negation, there will be always an odd number
# if(not(len(logic_array) % 2 == 1)):
# 	print("Array needs odd number of items")
# 	exit()

# num_turns = int(len(logic_array)/2 - 1)
num_turns = int(len(being) - 1)
print(num_turns)
radius = 1
pitch = 1.5

# num_half_turns = num_turns * 2
num_fifth_turns = num_turns * 5
print(num_fifth_turns)
# t = np.linspace(0, num_half_turns * np.pi, 2*num_half_turns+1)
t = np.linspace(0, 2 * num_turns * np.pi, num_fifth_turns + 1)
print(t)
x = radius * np.cos(t)
y = radius * np.sin(t)
z = pitch * t


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='Thought\'s path')

# add text labels
# for i, txt in enumerate(np.arange(0, num_half_turns+1, 0.5)):
print("Arange: 0 -> 0.2 -> " + str(num_fifth_turns))
for i, txt in enumerate(np.arange(0, num_fifth_turns-1)):
	print("Test: " + str(i))
	if i == 0:
		ax.text(x[i], y[i], z[i], being[0], color='red')
	if i % 5 == 0: # only label every other half turn
		# ax.text(x[i], y[i], z[i], logic_array[int(i / 2)], color='red')
		print(str(i) + " | div " + str(int(i/5)) )
		ax.text(x[i+1], y[i+1], z[i+1], nothing[int(i / 5)], color='red')
		ax.text(x[i+2], y[i+2], z[i+2], unity[int(i / 5)], color='red')
		ax.text(x[i+3], y[i+3], z[i+3], explicit[int(i / 5)], color='red')
		ax.text(x[i+4], y[i+4], z[i+4], negation[int(i / 5)], color='red')
		ax.text(x[i+5], y[i+5], z[i+5], being[int(i / 5)+1], color='red')

ax.legend()
plt.show()