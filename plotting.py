import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.collections import PatchCollection

def plot_lot(arrangement):


	board_switcher = [ [0,5], [1,5], [2,5], [3,5], [4,5], [5,5]
						 ,[0,4], [1,4], [2,4], [3,4], [4,4], [5,4]
						 ,[0,3], [1,3], [2,3], [3,3], [4,3], [5,3]
						 ,[0,2], [1,2], [2,2], [3,2], [4,2], [5,2]
						 ,[0,1], [1,1], [2,1], [3,1], [4,1], [5,1]
						 ,[0,0], [1,0], [2,0], [3,0], [4,0], [5,0] ]


	plt.close() # since we're going to be calling plot_lot() iteratively, close the last iteration before doing anything
	fig, ax = plt.subplots() # create a new figure and axis
	plt.axis([0, 6, 0, 6]) # set zoom/window of graph
	ax.set_axis_bgcolor('0.6') # color parking lot
	plt.gca().axes.xaxis.set_ticklabels([]) # remove xaxis labels
	plt.gca().axes.yaxis.set_ticklabels([]) # remove yaxis labels


	line = mlines.Line2D([6,6],[3,4],lw=15., alpha=0.8, color='yellow') # define a yellow line to indicate the exit
	ax.add_line(line) # add line to graph

	patches = []
	for i,vehicle in enumerate(arrangement):

		difference = vehicle[1] - vehicle[0] # get the difference b/n first and second squares that vehicle occupies
		if difference > 0:
			if abs(difference) == 1: # determine whether or not vehicle is horizontally oriented
				height = 1 # it's horizontal, so its height is 1
				width = len(vehicle) # it's horizontal, so its width is its length
				location = board_switcher[vehicle[0]]
			else: # vehicle must be vertically oriented
				height = len(vehicle) # it's vertical, so its height is its length
				width = 1 # it's vertical, so its width is 1
				location = board_switcher[vehicle[-1]]
		else:
			if abs(difference) == 1: # determine whether or not vehicle is horizontally oriented
				location = board_switcher[vehicle[-1]]
				height = 1 # it's horizontal, so its height is 1
				width = len(vehicle) # it's horizontal, so its width is its length
			else: # vehicle must be vertically oriented
				location = board_switcher[vehicle[0]]
				height = len(vehicle) # it's vertical, so its height is its length
				width = 1 # it's vertical, so its width is 1

		if i == 0:
			patches.append(mpatches.Rectangle(location, width, height, color='r')) # if this vehicle is the hero, color red
		else:
			patches.append(mpatches.Rectangle(location, width, height)) # otherwise just go with the default color
		



	collection = PatchCollection(patches, alpha=0.3, match_original=True)
	ax.add_collection(collection)
	plt.pause(0.7) # pause for 0.7 seconds between each frame so that humans can see what's happening
