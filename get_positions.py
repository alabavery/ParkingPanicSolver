# returns a tuple of all_vehicle_positions, starting_indices
def all_positions_and_starting_indices(starts): # starts is a list of lists, a list the lists of squares in which each vehicle starts

	ROWS_COLUMNS = (range(0,6),range(6,12),range(12,18),range(18,24),range(24,30),range(30,36)
					,range(0,31,6),range(1,32,6),range(2,33,6),range(3,34,6),range(4,35,6),range(5,36,6))

	def generate_vehicle(position):
		for rc in ROWS_COLUMNS:
			if position[0] in rc and position[1] in rc:
				r = rc
				break
		return (r,len(position))


	def generate_a_vehicles_positions(vehicle):
		this_vehicle_positions = []
		i = 0
		limit = 6 - vehicle[1]

		while i <= limit:
			if vehicle[1] == 2:
				this_vehicle_positions.append([vehicle[0][i], vehicle[0][i+1]] )
			else:
				this_vehicle_positions.append([vehicle[0][i], vehicle[0][i+1], vehicle[0][i+2]])
			i+=1

		assert 4 <= len(this_vehicle_positions) <= 5
		return this_vehicle_positions

	all_positions = []
	all_starting_indices = []


	for start in starts:
		vehicle = generate_vehicle(start)
		these_positions = generate_a_vehicles_positions(vehicle)
		all_positions.append(these_positions)
		
		for i,position in enumerate(these_positions):

			if position == start:
				all_starting_indices.append(i)

	return all_positions, all_starting_indices
