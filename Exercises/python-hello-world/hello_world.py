#
# Skeleton file for the Python "Hello World" exercise.
#

import re

class hello_world:
	def __init__(self, text):
		self.text = text

	def hello(text):
		if re.split(' ', text)[1] != 'World!':
			return text[1]
		else:
			return 'Hello World!'


