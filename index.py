from getPositions import all_positions_and_starting_indices
from optimize import optimize_arrangements
from plotting import plot_lot

level1 = [[12,13],[0,6],[1,2,3],[8,9],[10,11],[14,20],[18,19],[21,27,33],[24,25,26],[30,31,32],[28,34],[29,35]]
all_vehicle_positions, starting_vehicle_indices = all_positions_and_starting_indices(level1)

starting_level = starting_vehicle_indices[0]
visited = []

starting_occupation_array = [0] * 36
for i,svi in enumerate(starting_vehicle_indices):
	for square in all_vehicle_positions[i][svi]:
		starting_occupation_array[square] = 1

active_arrangement = ArrangementNode(None, all_vehicle_positions, starting_vehicle_indices, starting_occupation_array, starting_level, visited)
optimize_this = []
optimize_this.append(active_arrangement.vehicle_position_indices)
while active_arrangement.level != 4:
	active_arrangement = active_arrangement.return_new_arrangement()
	optimize_this.append(active_arrangement.vehicle_position_indices)


optimized = optimize_arrangements(optimize_this)
for vpi in optimized:

	positions = []
	for i,index in enumerate(vpi):
		positions.append(all_vehicle_positions[i][index])
	plot_lot(positions)

	
	



