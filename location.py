# ITERATION 0
class Location:
	"""
	Location class for representing buildings, etc.
	"""
	def __init__(self):
		"""Constructor for Location class."""
		self.x = 0
		self.y = 0
		self.name = ""
	

# 22.2 clicker question
s = Location()
s.name = "Severance"
s.x = 5
k = Location()
k.name = "King"
p = "Peters"

print(k.name + " is at " + str(k.x) + ", " + str(k.y))


# ITERATION 1+
class Location:
	"""
	Location class for representing buildings, etc.
	"""
	def __init__(self, x, y, n):
		"""Constructor for Location class."""
		self.x = x
		self.y = y
		self.name = n	
		
    # 22.4 Activity: Add method, attributes, etc. based on class discussion
	# def ...

# Activity: Create another instance and call method based on class discussion
t = Location(2, 1, "Tappan Square")

# Activity: Print to see if object is working as intended
print("TODO")