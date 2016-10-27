# consumes two vehicle position indices lists
# returns true if direct move, false if not
# direct move is defined as 
def test_direct_move(vpi1, vpi2):
	differences = 0
	for i in range(0, len(vpi1)):
		
		differences += abs(vpi1[i] - vpi2[i])

		if differences > 1:
			return False

	if differences == 1:
		return True
	else:
		return False	



# conusumes list of lists of vehicle position indices
# returns (hopefully shorter) list of lists of vehicle position indices
def optimize_arrangements(veh_pos_indices_list):
	optimized_list = [veh_pos_indices_list[0]] # start the optimized list with the starting arrangement

	while optimized_list[-1][0] != 4: # continue loop until you have a 'level 4' arrangement in optimized list (this will be the last arrangement represented by veh_pos_indices_list)

		backwards_iterator = -1
		while test_direct_move(veh_pos_indices_list[backwards_iterator], optimized_list[-1]) is False: # continue working backwards from the end of veh_pos_indices_list until you get a representation of an arr that is a direct move from the one at the end of optimized_list
			backwards_iterator -= 1

		optimized_list.append(veh_pos_indices_list[backwards_iterator])


	return optimized_list