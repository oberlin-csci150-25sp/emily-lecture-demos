iClicker = {'Molly': [1,0,1], 'Adam':[1,1,1], 'Sam':[0,1,1], 'Emily':[1,1,1]}

print(type(iClicker.keys()))
print(iClicker.values())

# putting the loop sequence into alphabetical order
# https://docs.python.org/3/howto/sorting.html

for k in sorted(iClicker.keys()):
	print(k + ": " + str(iClicker[k]))
