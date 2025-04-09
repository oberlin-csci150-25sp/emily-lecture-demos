class Product:
  def __init__(self, n, p):
    self.name = n 		# name as string 
    self.price = p 	  # dollars as float

  def get_name(self):
    return self.name

  def get_price(self):
    return self.price

  def set_price(self, new_p):
    self.price = new_p
    return
