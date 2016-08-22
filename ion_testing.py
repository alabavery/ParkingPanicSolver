import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


plt.ion()
plt.axis([0, 10, 0, 10])



for i in range(10):
	fig, ax = plt.subplots()
	plt.axis([0, 10, 0, 10])
	
	rect = mpatches.Rectangle([i,0],5,5)
	patches = []
	patches.append(rect)
	collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
	ax.add_collection(collection)
	plt.pause(0.5)

    #y = np.random.random()
    #plt.scatter(i, y)
#while True:
#    plt.pause(0.05)