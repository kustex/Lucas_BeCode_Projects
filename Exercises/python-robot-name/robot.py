import random
import string

class Robot:
	
	existing_names = []
	
	def randomize_name(self):
		while True:
			name = "".join(random.choice(string.ascii_uppercase) for _ in range(2))
			name += "".join(random.choice(string.digits) for _ in range(3))
			if name not in self.existing_names:
				self.existing_names.append(name)
				return name

	def __init__(self):
		self.name = self.randomize_name()

	def reset(self):
		self.name = self.randomize_name()

		
