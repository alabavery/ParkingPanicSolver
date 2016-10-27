import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

def plot_lot(arrangement):


	board_switcher = [ [0,5], [1,5], [2,5], [3,5], [4,5], [5,5]
						 ,[0,4], [1,4], [2,4], [3,4], [4,4], [5,4]
						 ,[0,3], [1,3], [2,3], [3,3], [4,3], [5,3]
						 ,[0,2], [1,2], [2,2], [3,2], [4,2], [5,2]
						 ,[0,1], [1,1], [2,1], [3,1], [4,1], [5,1]
						 ,[0,0], [1,0], [2,0], [3,0], [4,0], [5,0] ]


	plt.close()
	fig, ax = plt.subplots()
	plt.axis([0, 6, 0, 6])

	patches = []
	for i,vehicle in enumerate(arrangement):

		difference = vehicle[1] - vehicle[0]
		if difference > 0:
			if abs(difference) == 1:
				height = 1
				width = len(vehicle)
				location = board_switcher[vehicle[0]]
			else:
				height = len(vehicle)
				width = 1
				location = board_switcher[vehicle[-1]]
		else:
			if abs(difference) == 1:
				location = board_switcher[vehicle[-1]]
				height = 1
				width = len(vehicle)
			else:
				location = board_switcher[vehicle[0]]
				height = len(vehicle)
				width = 1

		if i == 0:
			patches.append(mpatches.Rectangle(location, width, height, color='r'))
		else:
			patches.append(mpatches.Rectangle(location, width, height))
		



	collection = PatchCollection(patches, alpha=0.3, match_original=True)
	ax.add_collection(collection)
	plt.pause(0.7)
