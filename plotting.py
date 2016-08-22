import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

def plot_lot(situation):
	plt.close()
	fig, ax = plt.subplots()
	plt.axis([0, 6, 0, 6])

	patches = []
	for vehicle in situation.vehicles:
		patches.append(vehicle.rectangle_patch)
		plt.text(vehicle.location[0] + 0.5,vehicle.location[1] + 0.5,vehicle.vehicle_name)

	for ps in situation.parking_lot:
		patches.append(ps.rectangle_patch)

	collection = PatchCollection(patches, alpha=0.3, match_original=True)
	ax.add_collection(collection)
	plt.pause(0.7)
