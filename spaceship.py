class Spaceship:
    def __init__(self, name):
        '''constructor for a Spaceship class'''
        '''name, speed, hasLasers by default'''
        self.name = name
        self.speed = 1000 
        self.hasLasers = True
    
    def getSpeed(self):
        '''returns the current speed value'''
        return self.speed
    
    def setSpeed(self, newSpeed):
        '''overrides speed to newSpeed value'''
        self.speed = newSpeed
    
    def hitByAsteroid(self):
        '''reduces speed and breaks lasers'''
        self.speed = self.speed - 100
        self.hasLasers = False 
    
    def __str__(self):
        '''converts Spaceship into a string for print statement convenience'''
        s = "The speed is: " + str(self.getSpeed())
        return s
    
    # continue next time!
    # def __lt__(???):
    #     '''overrides less than operator'''
    #     return ??? 

def main():
    # Create instances
    sparrow = Spaceship('sparrow')
    owl = Spaceship('owl')

    # Given example: Test getSpeed() method
    print(sparrow.getSpeed())

    # Test setSpeed() method
    sparrow.setSpeed(50)
    print(sparrow.getSpeed())

    # Test hitByAsteroid() method
    owl.hitByAsteroid()
    print("owl speed:", owl.getSpeed())
    print("owl lasers:", owl.hasLasers)

    # What happens when we try to print an instance of a user-defined class?
    print(owl)
    print(sparrow)

if __name__ == "__main__":
    main()