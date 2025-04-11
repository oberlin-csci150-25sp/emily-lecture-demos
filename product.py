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

class Tea(Product):
  def __init__(self, n, p, c):
    super().__init__(n, p)
    self.caffeine_level = c

# class Ceramics(Product):
#   pass

class Fruit(Product):
  def __init__(self, n, p, q):
    super().__init__(n, p)
    self.quantity = q
  
  def get_quantity(self):
    return self.quantity
  
  def new_quantity(self, new_q):
    self.quantity = new_q

class Cookie(Product):
  def __init__(self, n, p, s, a):
    super().__init__(n, p)
    self.stock = s
    self.allergen = a
  
  def show_allergen(self):
    return self.allergen
  
def main():
  # make test instances of each specific product
  # show price
  pbcookie = Cookie("peanut butter cookie", 3, 50, "peanuts")
  print(pbcookie.get_price())

  apple = Fruit("apple", 1, 20)
  print(apple.get_price())

  earlgrey = Tea("earl grey", 4, "high")
  eg_price = earlgrey.get_price()
  print(eg_price)

if __name__ == "__main__":
  main() 