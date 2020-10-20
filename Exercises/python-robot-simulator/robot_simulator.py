NORTH = "North"
EAST = "East"
SOUTH = "South"
WEST = "West"

class Robot:
	
	def __init__(self, bearing=NORTH, x=0, y=0):
		self.bearing = bearing
		self.coordinates = (x,y)

	def advance(self):
		if self.bearing == NORTH:
			self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
		if self.bearing == EAST:
			self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
		if self.bearing == SOUTH:
			self.coordinates = (self.coordinates[0], self.coordinates[1] -1)
		if self.bearing == WEST:
			self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

	def turn_left(self):
		if self.bearing == NORTH:
			self.bearing = WEST
		elif self.bearing == WEST:
			self.bearing = SOUTH
		elif self.bearing == SOUTH:
			self.bearing = EAST
		elif self.bearing == EAST:
			self.bearing = NORTH

	def turn_right(self):
		if self.bearing == NORTH:
			self.bearing = EAST
		elif self.bearing == EAST:
			self.bearing = SOUTH
		elif self.bearing == SOUTH:
			self.bearing = WEST
		elif self.bearing == WEST:
			self.bearing = NORTH
	
	def simulate(self, seq):
		for i in seq:
			if i == "L":
				self.turn_left()
			if i == "R":
				self.turn_right()
			if i == "A":
				self.advance()
	

