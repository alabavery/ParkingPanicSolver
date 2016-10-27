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

