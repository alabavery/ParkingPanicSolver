from vehicles_and_lot import Vehicle, ParkingSquare, get_spaces_in_location
from random import randrange, choice

def generate_lot(num_vehicles):

	PARKING_LOT = []
	for x in range(10):
		for y in range(10):
			ps = ParkingSquare([x,y])
			PARKING_LOT.append(ps)
			if x == 9 and y == 2:
				exit = ps


	names = ["V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17"]
	vehicles = []

	hero = Vehicle("HERO",PARKING_LOT,[1,2,2,1],"x","yellow")
	vehicles.append(hero)
	while len(vehicles) < num_vehicles:
		facecolor = choice(["red","green","blue","purple","orange","maroon"])
		try:
			name = names[names.index(vehicles[-1].vehicle_name) + 1]
		except:
			name = "V2"

		x_coord = randrange(0,8)
		y_coord = randrange(0,8)
		if y_coord == 2:
			length = 1
		else:
			length = randrange(1,4)
		if length > 1:
			width = 1
			mvt_axis = "x"
		else:
			width = randrange(2,4)
			mvt_axis = "y"

		location = [x_coord,y_coord,length,width]
		spaces = get_spaces_in_location(PARKING_LOT,location)
		bad = False
		if spaces == "Off the map":
			bad = True
		else:
			for ps in spaces:
				if ps.vehicle_occupant != None:
					bad = True
		if bad == True:
			continue

		v = Vehicle(name, PARKING_LOT,location,mvt_axis,facecolor)
		vehicles.append(v)


	return PARKING_LOT,vehicles,hero,exit
