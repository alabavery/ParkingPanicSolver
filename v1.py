class ArrangementNode():



	def __init__(self, parent_arrangement, all_vehicle_positions, vehicle_position_indices, occupation_array, level, visited):
		self.parent_arrangement = parent_arrangement
		self.all_vehicle_positions = all_vehicle_positions
		self.vehicle_position_indices = vehicle_position_indices
		self.occupation_array = occupation_array
		self.level = level

		visited.append(self.vehicle_position_indices)
		self.visited = visited


	# called by self.test_move()
	# consumes movement  = (index of vehicle to move, square left, square entered)
	def get_new_position_indices(self, movement):
		new_position_indices = list(self.vehicle_position_indices)
		
		for i in range(0,len(new_position_indices)):
			if i == movement[0]:
				if movement[1] < movement[2]:
					new_position_indices[i] += 1
				else:
					new_position_indices[i] -= 1

		return new_position_indices


	# called by self.test_move()
	# consumes new_move = (vehicle_index, vehicle_leaves_square, vehicle_enters_square)
	# returns list of 0s and 1s signifying occupation
	def get_new_occupation_array(self, new_move):
		new_occupation_array = list(self.occupation_array) #self.occupation_array is a one dimensional, 36 item array of ints representing parking squares
		new_occupation_array[new_move[1]] = 0 # set the square that the moved vehicle left to 0
		new_occupation_array[new_move[2]] = 1 # ensure the square that the moved vehicle newly occupies is 1
		return new_occupation_array



	# called by self.find_valid_move()
	# calls self.get_new_position_indices(), self.get_new_occupation_array() 
	# consumes int, int
	# returns (new_position_indices, new_occupation_array) if successful, None if unsuccessful
	def test_move(self, vehicle_index, direction):
		if direction > 0:
			if len(self.all_vehicle_positions[vehicle_index]) > self.vehicle_position_indices[vehicle_index]+1:
				vehicle_leaves_square = self.all_vehicle_positions[vehicle_index][self.vehicle_position_indices[vehicle_index]][0]
				vehicle_enters_square = self.all_vehicle_positions[vehicle_index][self.vehicle_position_indices[vehicle_index]+1][-1]
			else:
				return None
		else:
			if self.vehicle_position_indices[vehicle_index] > 0:
				vehicle_leaves_square = self.all_vehicle_positions[vehicle_index][self.vehicle_position_indices[vehicle_index]][-1]
				vehicle_enters_square = self.all_vehicle_positions[vehicle_index][self.vehicle_position_indices[vehicle_index]-1][0]
			else:
				return None

		if self.occupation_array[vehicle_enters_square] == 0: # check if the intended square is occupied - will be 0 if no
			new_move = (vehicle_index, vehicle_leaves_square, vehicle_enters_square)
			new_position_indices = self.get_new_position_indices(new_move)

			if new_position_indices not in self.visited:
				new_occupation_array = self.get_new_occupation_array(new_move)
				return new_position_indices, new_occupation_array



	# called by self.return_new_arrangement()
	# calls self.test_move()
	# returns new position indices if successful, None if unsuccessful
	def find_valid_move(self):
		npi_noa = self.test_move(0,1) # first try hero forward, that's this line
		
		if npi_noa is None: # if didn't work new_indices will be Nonetype
			
			for vehicle in range(0,len(self.vehicle_position_indices)):
				npi_noa = self.test_move(vehicle, 1) # try to move each vehicle 'forward'
				if npi_noa is not None: # if didn't work new_indices will be Nonetype
					break

			if npi_noa is None: # if no 'forward' moves worked then try to move each 'backwards'
				for vehicle in range(0,len(self.vehicle_position_indices)):
					npi_noa = self.test_move(vehicle, -1)
					if npi_noa is not None:
						break

				if npi_noa is None:
					npi_noa = self.test_move(0,-1)

		return npi_noa



	# called by index
	# calls self.find_valid_move()
	# returns Arrangement()
	def return_new_arrangement(self):
		npi_noa = self.find_valid_move()
		if npi_noa is None:
			return self.parent_arrangement

		# def __init__(self, parent_arrangement, all_vehicle_positions, vehicle_position_indices, occupation_array, level, visited)
		return ArrangementNode(self, self.all_vehicle_positions, npi_noa[0], npi_noa[1], npi_noa[0][0], self.visited)







all_vehicle_positions = [
							[[12, 13], [13, 14], [14, 15], [15, 16], [16, 17]], 
							[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], 
							[[0, 6, 12], [6, 12, 18], [12, 18, 24], [18, 24, 30]], 
							[[0, 6], [6, 12], [12, 18], [18, 24], [24, 30]], 
							[[3, 9, 15], [9, 15, 21], [15, 21, 27], [21, 27, 33]], 
							[[5, 11, 17], [11, 17, 23], [17, 23, 29], [23, 29, 35]], 
							[[30, 31, 32], [31, 32, 33], [32, 33, 34], [33, 34, 35]], 
							[[24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]
						]

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

	
	


