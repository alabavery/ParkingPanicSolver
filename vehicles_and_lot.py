import matplotlib.patches as mpatches
from random import choice
from time import sleep

#this function returns the ParkingSquare instances corresponding to a given location
def get_spaces_in_location(parking_lot,location):
	x_coords = range(location[0],location[0] + location[2])
	y_coords = range(location[1],location[1] + location[3])
	
	spaces = []
	for x in x_coords:
		for y in y_coords:

			#This is where you will get an error if you try to move a Vehicle off the map.
			try:
				ps = [p for p in parking_lot if p.coordinates == [x,y]][0]
				spaces.append(ps)
			#This return should only be handled by identify obstructions
			except IndexError:
				return "Off the map"

	return spaces



class ParkingSquare():
	#coordinates is a list of the left X and bottom y coords: [left_x,bottom_y]
	def __init__(self,coordinates):
		self.coordinates = coordinates
		self.vehicle_occupant = None
		self.rectangle_patch = mpatches.Rectangle([coordinates[0],coordinates[1]],1,1,facecolor='grey')
		self.hypothetical_occupant = None


class Vehicle():


	#location is list: [left_x,bottom_y,width,height]
	#axis_of_movement is either 'x' or 'y'
	def __init__(self,vehicle_name,parking_lot,location,axis_of_movement,facecolor,edgecolor="black",linewidth=5):
		self.vehicle_name = vehicle_name
		self.location = location
		self.hypothetical_location = location
		
		self.facecolor = facecolor
		self.edgecolor = edgecolor
		self.linewidth = linewidth

		if axis_of_movement == 'x':
			self.movement_vector = [1,0]
		else:
			self.movement_vector = [0,1]
		self.parking_lot = parking_lot
		#mpatches.Rectangle takes ([x coord of left side,y coord of bottom],width,height)
		self.rectangle_patch = mpatches.Rectangle([location[0],location[1]],location[2],location[3],facecolor=facecolor,edgecolor=edgecolor,linewidth=linewidth)

		spaces = get_spaces_in_location(parking_lot,location)
		self.occupied_spaces = spaces
		self.hypothetical_spaces = spaces
		for space in spaces:
			space.vehicle_occupant = self
			space.hypothetical_occupant = self



	#location is list: [left_x,bottom_y,width,height]
	def identify_obstructions(self,parking_lot,intended_location):

		intended_spaces = get_spaces_in_location(parking_lot,intended_location)
		if intended_spaces == "Off the map":
			return intended_spaces

		obstructions = []
		for space in intended_spaces:
			#if not (space.vehicle_occupant == None or space.vehicle_occupant == self):
			if not (space.hypothetical_occupant == None or space.hypothetical_occupant == self):
				obstructions.append([space,space.hypothetical_occupant])
				print("Can't move ",self.vehicle_name,"to occupy",space.coordinates,"; ",space.hypothetical_occupant.vehicle_name,"is hypothetically occupying that space.")

		return obstructions


	#movement is a list of the deltas to x and y; note that in practice only 1 coordinate can be changed (because
	#that's how the game is played), so one of the deltas is always zero.  e.g.: [-1,0]
	#move either moves the vehicle and returns True or does nothing and returns a list of obstructions preventing the movement
	def test_move(self,movement):
		intended_location = [self.location[0] + movement[0],self.location[1] + movement[1],self.location[2],self.location[3]]

		obstructions = self.identify_obstructions(self.parking_lot,intended_location)
		if obstructions == "Off the map":
			print("Testing moving", self.vehicle_name, " The move would be off the map...")
			return "Off the map"


		#intended_spaces = get_spaces_in_location(self.parking_lot,intended_location)
		#for space in self.hypothetical_spaces:
		#	space.hypothetical_occupant = None		
		#for space in intended_spaces:
		#	space.hypothetical_occupant = self


		if len(obstructions) == 0:
			return True, intended_location
		else:
			return False, obstructions



	def move(self,new_location):
		new_spaces = get_spaces_in_location(self.parking_lot,new_location)
		
		for ps in self.occupied_spaces:
			ps.vehicle_occupant = None
		for space in new_spaces:
			space.vehicle_occupant = self
			space.hypothetical_occupant = self

		self.location = new_location
		self.hypothetical_location = new_location
		self.occupied_spaces = new_spaces
		self.hypothetical_spaces = new_spaces
		self.rectangle_patch = mpatches.Rectangle([self.location[0],self.location[1]],self.location[2],self.location[3],facecolor=self.facecolor,edgecolor=self.edgecolor,linewidth=self.linewidth)
