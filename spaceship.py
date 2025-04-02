class Spaceship:
    def __init__(self, name):
        '''constructor for a Spaceship class'''
        self.name = name
        self.speed = 1000 
        self.hasLasers = True
    
    def getSpeed(self):
        '''add docstring here'''
        return self.speed
    
    def setSpeed(self, newSpeed):
        '''add docstring here'''
        self.speed = newSpeed
    
    def hitByAsteroid(self):
        '''add docstring here'''
        self.speed = self.speed - 100
        self.hasLasers = False 

def main():
    # Create instances
    sparrow = Spaceship('sparrow')
    owl = Spaceship('owl')

    # Given example: Test getSpeed() method
    print(sparrow.getSpeed())

    # TODO: Test setSpeed() method

    # TODO: Test hitByAsteroid() method

    # TODO: What happens when we try to print an instance of a user-defined class?

if __name__ == "__main__":
    main()