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

    # location box (e.g., property perimeter)
    self.box = [] # list of coordinates

    # ratings
    self.ratings = [] # nested list of rating text and numbers [["review", 5]]
    
   # 22.4 Activity: Add method, attributes, etc. based on class discussion. 
   # Use case? Attributes? Methods?
   # def ...

# Activity: Create another instance and call method based on class discussion
t = Location(2, 1, "Tappan Square")

# Activity: Print to see if object is working as intended
print(t)
print(t.x, t.y, t.name, t.box, t.ratings)