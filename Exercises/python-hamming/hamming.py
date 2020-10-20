def distance(self, text, text1):
	counter = 0
	for i in range(len(text)): 
		if text[i] != text1[i]: 
			counter += 1
	return counter
