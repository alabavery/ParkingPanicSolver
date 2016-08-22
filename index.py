import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

from vehicles_and_lot import ParkingSquare, Vehicle
from ai_player import Situation
from plotting import plot_lot
from generate_game import generate_lot

from time import sleep



PARKING_LOT = []
for x in range(6):
	for y in range(6):
		ps = ParkingSquare([x,y])
		PARKING_LOT.append(ps)
		if x == 5 and y == 3:
			exit = ps

VEHICLES = [
	Vehicle("HERO",PARKING_LOT,[1,3,2,1],'x','red')
	,Vehicle("V2",PARKING_LOT,[2,0,2,1],'x','blue')

	,Vehicle("V3",PARKING_LOT,[1,0,1,2],'y','yellow')
	,Vehicle("V4",PARKING_LOT,[1,2,2,1],'x','green')
	,Vehicle("V5",PARKING_LOT,[3,1,1,3],'y','orange')
	,Vehicle("V6",PARKING_LOT,[5,0,1,3],'y','magenta')
]
hero = [v for v in VEHICLES if v.vehicle_name == "HERO"][0]

#PARKING_LOT,VEHICLES,hero,exit = generate_lot(20)
game = Situation(PARKING_LOT,VEHICLES,hero,exit)


plt.ion()
plt.axis([0, 10, 0, 10])
plot_lot(game)

while game.exit.vehicle_occupant != game.hero:
	game.make_plan()
	for a_move in game.move_queue:
		a_move[0].move(a_move[1])
		plot_lot(game)

print()
print()
print("Level Completed!!!!!!")
sleep(10)







