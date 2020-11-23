import random
import numpy as np
import matplotlib.pyplot as plt

vals = []

for i in range(100000):
	vals += [random.randrange(1, 7, 1) + random.randrange(1, 7, 1)]

freq, bins, patches = plt.hist(vals, 11, edgecolor='white', color='#8a40b8')
plt.xlabel('dice roll',fontsize=12)
plt.ylabel('frequency',fontsize=12)

bin_centers = np.diff(bins)*0.5 + bins[:-1]
n = 0
for fr, x, patch in zip(freq, bin_centers, patches):
  height = int(freq[n])
  plt.annotate("{}".format(round((height/len(vals)), 3)),
    xy = (x, height),             # top left corner of the histogram bar
    xytext = (0,0.2),             # offsetting label position above its bar
    textcoords = "offset points", # Offset (in points) from the *xy* value
    ha = 'center', va = 'bottom')
  n = n+1

plt.text(2, 16000, 'labels on top of bars represent', fontsize=8)
plt.text(2, 15500, 'the probability of dice roll', fontsize=8)

plt.savefig("plot.png")
plt.clf()