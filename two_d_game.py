'''
Alan Wen
Assignment 10.1
custom class
a class that is modeled from a real world object 
    at least 1 class variable
    at least 2 data variables
    at least 2 get-set methods
        methods that access variables 
    2 other methods that do not include get-set methods
        DYLAN SAID IN DISCORD THAT IT'S TWO OF THESE TOTAL NOT A PAIR OF EACH KIND 
I will be trying to create a "2d game" where "players" can move along the x-y axis 
"if you write proper instructions for it, and the class meets all requirements, you're fine"
-Hari
he said that in the discord on december 1st ik this class is kinda boring in retrospect but teacher man said I could do it so I don't care 
'''

class Position:
    #all players can move
    movement = True
    def __init__ (self, x = 0 , y  = 0, dspeed = 1):
        #initialize variables like coordinates and speed at the beginning
        self._coordinates = [x , y]
        self._speed = dspeed
    
    def move(self , direction):
        #moving function that will make a player object move in directions when given commands in the terminal
        if direction == "left":
            self._coordinates[0] -= self._speed
        elif direction == "right":
            self._coordinates[0]+= self._speed
        elif direction == "up":
            self._coordinates[1] += self._speed
        elif direction == "down": 
            self._coordinates[1] -= self._speed
        else:
            print("invalid direction")
            return None
    def change_speed(self , command):
        # change speed depending on the given command
        if command == "run": 
            self._speed = 2
        elif command == "walk": 
            self._speed = 1
    def get_coordinates(self): 
        #return the list that has been edited by move method
        return self._coordinates
    def get_speed(self):
        #return the speed value that can be edited by the change speed method
        return self._speed
    
#main
def main():
    #demo program
    #create object p1
    p1 = Position()
    #access default stats
    print(p1.get_coordinates())
    print(p1.get_speed())
    #move up and right with default walking speed and access coordinates
    p1.move("right")
    p1.move("up")
    print(p1.get_coordinates())
    #start running
    p1.change_speed("run")
   # run to the left and access stats
    p1.move("left")
    print(p1.get_coordinates())
    print(p1.get_speed())
    #create object p2
    p2 = Position()
    #p2 starts running
    p2.change_speed("run")
    p2.move("up")
    p2.move("up")
    p2.move("right")
    #access p2 coordinates after moving up twice and right once while running 
    print(p2.get_coordinates())
#call main 
if __name__ == "__main__":
    main()