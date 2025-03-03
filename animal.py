import random

print('Welcome to the text animal generator!')

# randomly select one of the premade animals
choice = random.randint(0, 2)

animal = ''
if choice == 0:
	animal = '_/\__/\__0>' # worm
elif choice == 1:
	animal = '=^..^=' # cat
else:
	animal = '(0.0)' # owl

print(animal)