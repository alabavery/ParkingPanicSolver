from vehicles_and_lot import get_spaces_in_location

class Situation():

	def __init__(self,parking_lot,vehicles,hero,exit):
		#parking_lot is a list of ParkingSquares
		self.parking_lot = parking_lot
		#vehicles is a list of Vehicles
		self.vehicles = vehicles
		#hero is a Vehicle
		self.hero = hero
		#exit is a ParkingSquare
		self.exit = exit
		self.move_queue = []
		self.move_queue_record = []

	#  feed this function a list of ParkingSquare and the Vehicle that needs to clear it; first_clearance is a list
	#  of ParkingSquare and the Vehicle that needs to clear it
	def clear_path(self,first_clearance):
		
		move_queue = []
		this_clearance = first_clearance

		#the loop will run until a move that does not require another Vehicle to move is found
		while True:
			print()
			print("New iteration of clear_path loop...")

			#sqr to clear will be a ParkingSquare
			sqr_to_clear = this_clearance[0]
			#this_vehicle will be a Vehicle
			this_vehicle = this_clearance[1]

			#translation of line below: 'if axis of movement is x'
			if this_vehicle.movement_vector == [1,0]:
				#this_vehicle.location is a list of [left-most x coord (integer), bottom-most y coord (int), width (int), height (int)]
				#sqr_to_clr.coordinates is list of [left-most x coord, bottom-most y coord]
				#some_distance is difference b/n Vehicle left-most x and sqr_to_clear left-most x
				some_distance = this_vehicle.location[0] - sqr_to_clear.coordinates[0]
				#  possible_move_vectors give us the minimum distances required for the Vehicle move to no longer occupy the
				#  ParkingSquare.  Those distances change based on the relative positions of the Vehicle and ParkingSquare, hence
				#  the conditionals below. There are exactly two of these minimum distance vectors for a given pair of relative 
				#  positions because a Vehicle can only move in two directions, based on its axisofmovement aka movement vector.
				if abs(some_distance) == 0:
					possible_move_vectors = [[1,0],[-this_vehicle.location[2],0]]
				elif abs(some_distance) == 1:
					possible_move_vectors = [[2,0],[-this_vehicle.location[2] + 1,0]]
				else:
					possible_move_vectors = [[3,0],[-1,0]]
			#axis of movement is y
			else:
				#this_vehicle.location is a list of [left-most x coord (integer), bottom-most y coord (int), width (int), height (int)]
				#sqr_to_clr.coordinates is list of [left-most x coord, bottom-most y coord]
				#some_distance is difference b/n Vehicle left-most x and sqr_to_clear left-most x
				some_distance = this_vehicle.location[1] - sqr_to_clear.coordinates[1]
				#  possible_move_vectors give us the minimum distances required for the Vehicle move to no longer occupy the
				#  ParkingSquare.  Those distances change based on the relative positions of the Vehicle and ParkingSquare, hence
				#  the conditionals below. There are exactly two of these minimum distance vectors for a given pair of relative 
				#  positions because a Vehicle can only move in two directions, based on its axisofmovement aka movement vector.
				if abs(some_distance) == 0:
					possible_move_vectors = [[0,1],[0,-this_vehicle.location[3]]]
				elif abs(some_distance) == 1:
					possible_move_vectors = [[0,2],[0,-this_vehicle.location[3] + 1]]
				else:
					possible_move_vectors = [[0,3],[0,-1]]

			print()
			print("Going to test moving",this_vehicle.vehicle_name)

			test0 = this_vehicle.test_move(possible_move_vectors[0])
			try:
				print("test0: ",test0[0],"ParkingSquare: ",test0[1][0][0].coordinates,"; Vehicle: ",test0[1][0][1].vehicle_name)
			except:
				print("test0: ",test0)
			intended_location0 = [this_vehicle.hypothetical_location[0] + possible_move_vectors[0][0],this_vehicle.hypothetical_location[1] + possible_move_vectors[0][1],this_vehicle.location[2],this_vehicle.location[3]]
			intended_spaces0 = get_spaces_in_location(self.parking_lot,intended_location0)
			been_here0 = [1 for vm in self.move_queue_record if vm == [this_vehicle,intended_location0]]
			print("been_here0: ",been_here0)

			test1 = this_vehicle.test_move(possible_move_vectors[1])
			print("test1: ",test1)
			try:
				print("test1: ",test1[0],"ParkingSquare: ",test1[1][0][0].coordinates,"; Vehicle: ",test1[1][0][1].vehicle_name)
			except:
				print("test1: ",test1)
			intended_location1 = [this_vehicle.hypothetical_location[0] + possible_move_vectors[1][0],this_vehicle.hypothetical_location[1] + possible_move_vectors[1][1],this_vehicle.location[2],this_vehicle.location[3]]
			intended_spaces1 = get_spaces_in_location(self.parking_lot,intended_location1)
			been_here1 = [1 for vm in self.move_queue_record if vm == [this_vehicle,intended_location1]]
			print("been_here1: ",been_here1)

			
			def add_to_queue(this_vehicle,test,intended_location,intended_spaces,move_queue,move_queue_record):
				
				this_vehicle.hypothetical_spaces = intended_spaces
				this_vehicle.hypothetical_location = intended_location
				for space in intended_spaces:
					space.hypothetical_occupant = this_vehicle
				move_queue.append([this_vehicle,intended_location])
				move_queue_record.append([this_vehicle,intended_location])


			if test0 == "Off the map":
				print()
				print("Running 88 block")
				
				if test1 == "Off the map":
					print("#################################")
					print("No non-out-of-bounds moves")
					print("#################################")

				elif test1[0] == True:
					print("Running line 94 to move",this_vehicle.vehicle_name)
					add_to_queue(this_vehicle,test1,intended_location1,intended_spaces1,move_queue,self.move_queue_record)
					break

				else:
					print("Running line 99 to move",this_vehicle.vehicle_name)
					add_to_queue(this_vehicle,test1,intended_location1,intended_spaces1,move_queue,self.move_queue_record)
					this_clearance = test1[1][0]


			elif test1 == "Off the map":
				print()
				print("Running 105 block")
				print(this_vehicle.location)
				print(test0)

				if test0[0] == True:
					print("Running line 110 to move",this_vehicle.vehicle_name)		
					add_to_queue(this_vehicle,test0,intended_location0,intended_spaces0,move_queue,self.move_queue_record)
					print("Found Unobstructed move for",this_vehicle.vehicle_name)
					break

				else:
					print("Running line 116 to move",this_vehicle.vehicle_name)
					add_to_queue(this_vehicle,test0,intended_location0,intended_spaces0,move_queue,self.move_queue_record)
					this_clearance = test0[1][0]

			elif len(been_here0) > 0:
				print()
				print("Running 121 block")
				print("Established that been to",intended_location0)

				if test1[0] == True:
					print("Running line 125 to move",this_vehicle.vehicle_name)
					add_to_queue(this_vehicle,test1,intended_location1,intended_spaces1,move_queue,self.move_queue_record)
					break

				else:
					print("Running line 130 to move",this_vehicle.vehicle_name)
					add_to_queue(this_vehicle,test1,intended_location1,intended_spaces1,move_queue,self.move_queue_record)
					this_clearance = test1[1][0]


			elif test0[0] == True:
				print()
				print("Runing 136 block")
				print("Running line 137 to move",this_vehicle,vehicle_name)
				add_to_queue(this_vehicle,test0,intended_location0,intended_spaces0,move_queue,self.move_queue_record)
				print("Found Unobstructed move for",this_vehicle.vehicle_name)
				break

			elif len(been_here1) > 0:
				print()
				print("running 143 block")
				print("Established that been to",intended_location1)
				print("Running line 145 to move",this_vehicle.vehicle_name)
				add_to_queue(this_vehicle,test0,intended_location0,intended_spaces0,move_queue,self.move_queue_record)
				this_clearance = test0[1][0]				

			else:
				print()
				print("Running 153 block")
				if test1[0] == True:
					print("Running line 155 to move",this_vehicle.vehicle_name)
					"""new_location = [this_vehicle.location[0] + possible_move_vectors[1][0], this_vehicle.location[1] + possible_move_vectors[1][1], this_vehicle.location[2], this_vehicle.location[3]]
					
					this_vehicle.hypothetical_spaces = intended_spaces1
					for space in intended_spaces1:
						space.hypothetical_occupant = this_vehicle

					move_queue.append([this_vehicle,new_location])
					self.move_queue_record.append([this_vehicle,new_location])"""
					add_to_queue(this_vehicle,test1,intended_location1,intended_spaces1,move_queue,self.move_queue_record)
					break
				else:
					print("Running line 166 to move",this_vehicle.vehicle_name)
					"""new_location = [this_vehicle.location[0] + possible_move_vectors[1][0], this_vehicle.location[1] + possible_move_vectors[1][1], this_vehicle.location[2], this_vehicle.location[3]]
					
					this_vehicle.hypothetical_spaces = intended_spaces1
					for space in intended_spaces1:
						space.hypothetical_occupant = this_vehicle

					move_queue.append([this_vehicle,new_location])
					self.move_queue_record.append([this_vehicle,new_location])"""
					add_to_queue(this_vehicle,test1,intended_location1,intended_spaces1,move_queue,self.move_queue_record)
					this_clearance = test1[1][0]			

		"""




			elif test1[0] == False:
				if test0[0]:
					new_location = [this_vehicle.location[0] + possible_move_vectors[0][0], this_vehicle.location[1] + possible_move_vectors[0][1], this_vehicle.location[2], this_vehicle.location[3]]
					move_queue.append([this_vehicle,new_location])
					self.move_queue_record.append([this_vehicle,new_location])
					print("Found Unobstructed move for",this_vehicle.vehicle_name)
					break
				else:
					new_location = [this_vehicle.location[0] + possible_move_vectors[0][0], this_vehicle.location[1] + possible_move_vectors[0][1], this_vehicle.location[2], this_vehicle.location[3]]
					move_queue.append([this_vehicle,new_location])
					self.move_queue_record.append([this_vehicle,new_location])
					this_clearance = test0[1][0]			







			intended_location = [this_vehicle.location[0] + possible_move_vectors[0][0],this_vehicle.location[1] + possible_move_vectors[0][1],this_vehicle.location[2],this_vehicle.location[3]]
			been_here0 = [1 for vm in self.move_queue_record if vm == [this_vehicle,intended_location]]


			if len(been_here0) == 0 and test0[0] == True:
				new_location = [this_vehicle.location[0] + possible_move_vectors[0][0], this_vehicle.location[1] + possible_move_vectors[0][1], this_vehicle.location[2], this_vehicle.location[3]]
				move_queue.append([this_vehicle,new_location])
				self.move_queue_record.append([this_vehicle,new_location])
				print("Found Unobstructed move for",this_vehicle.vehicle_name)
				break

			test1 = this_vehicle.test_move(possible_move_vectors[1])
			intended_location = [this_vehicle.location[0] + possible_move_vectors[1][0],this_vehicle.location[1] + possible_move_vectors[1][1],this_vehicle.location[2],this_vehicle.location[3]]
			been_here1 = [1 for vm in self.move_queue_record if vm == [this_vehicle,intended_location]]
			if len(been_here1) == 0 and test1[0] == True:
				new_location = [this_vehicle.location[0] + possible_move_vectors[1][0], this_vehicle.location[1] + possible_move_vectors[1][1], this_vehicle.location[2], this_vehicle.location[3]]
				move_queue.append([this_vehicle,new_location])
				self.move_queue_record.append([this_vehicle,new_location])
				print("Found Unobstructed move for",this_vehicle.vehicle_name)
				break

			elif len(been_here0) == 0 and test0[0] == False:
				new_location = [this_vehicle.location[0] + possible_move_vectors[0][0], this_vehicle.location[1] + possible_move_vectors[0][1], this_vehicle.location[2], this_vehicle.location[3]]
				move_queue.append([this_vehicle,new_location])
				self.move_queue_record.append([this_vehicle,new_location])
				this_clearance = test0[1][0]

			elif len(been_here1) == 0 and test1[0] == False:
				new_location = [this_vehicle.location[0] + possible_move_vectors[1][0], this_vehicle.location[1] + possible_move_vectors[1][1], this_vehicle.location[2], this_vehicle.location[3]]
				move_queue.append([this_vehicle,new_location])
				self.move_queue_record.append([this_vehicle,new_location])
				this_clearance = test1[1][0]
			else:
				print("No non-out-of-bounds moves")
		"""
		print()
		print("The returned move_queue from clear_path() is:")
		for move in move_queue:
			print("Move",move[0].vehicle_name,"to",move[1])
		return move_queue


	#  .return_next_move() is the one and only function that calls make_plan().  Everytime return_next_move() is called,
	#  it will call make_plan() just one time - however, return_next_move() will only be called repeatedly in an iterative
	#  structure.  Therefore, .make_plan() should be thought of not as making the entire plan to solve the puzzle, but rather
	#  as a plan for solving miniature puzzles, the miniature puzzles being what moves are required at any given time to
	#  move the hero Vehicle one space right, toward the exit.
	def make_plan(self):
		print("\n")
		print("Clearing self.move_queue and making plan")
		self.move_queue = []
		hero_clear = self.hero.test_move([1,0])

		if hero_clear[0] == False:
			# the movement of hero was obstructed. Make a plan to clear the obstruction.
			# since the movement of the hero was obstructed, hero.test_move() returns a 
			# two-item list of [False,[list of lists of [obstructed ParkingSquare,obstructing Vehicle]]
			# so hero_clear[1] references that list of lists and hero_clear[1][0] 
			# references the first list of [obstructed PS, obstructing Vehicle] in the list of lists
			# So clearing_moves = self.make_plan([obstructed PS, obstructing Vehicle])
			print()
			print("Calling clear_path")
			clearing_moves = self.clear_path(hero_clear[1][0])
			reversed_cm = []
			for i in range(1,len(clearing_moves)+1):
				reversed_cm.append(clearing_moves[len(clearing_moves) - i])
			self.move_queue.extend(reversed_cm)
			print()
			print("Make_plan() set the move_queue to:")
			for move in self.move_queue:
				print("Move",move[0].vehicle_name,"to",move[1])

		else:
			print()
			print("Nothing obstructing hero's movement. Adding hero movement to queue.")
			# the movement of the hero is not obstructed, so our plan is simple; move the hero one space right.
			self.move_queue.append([self.hero,[self.hero.location[0]+1,self.hero.location[1],self.hero.location[2],self.hero.location[3]]])


