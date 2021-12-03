https://github.com/AlanHWen/Projects
# Projects
description: 
  a class that simulates a 2d map where objects can move along the x and y axis using different methods. Objects can "walk" or "run" if their speed is changed 
  and you can access their stats such as speed and coordinates at any time. 
class and data variables: 
  class variable movement: All objects are able to move around the map, so this variable is a boolean set to True.
  Data variables: 
    coordinates: the position on the x,y plane for an object. Displayed as a list.
    speed: the speed at which an object can move in one direction at a time. You can toggle between "run" and "walk" with commands which sets the speed variable to 2 and 1 
    respectively. 
methods: 
  move("direction"): takes in one of 4 different direction arguments as strings. ex: "left" "up" "right" "down" this method will change one of the coordinates depending on which string is
  passed. 
  change_speed("speed"): takes in one of 2 different string arguments. "walk" and "run" every object starts off with walk speed, and when "run" is passed the objects speed 
  is changed to 2. 
  get_coordinates(): returns the x-y coordinates of the string as a list 
  get_speed(): returns the speed of the object as an int

demo program description: 
  the demo program creates two objects p1 and p2. These objects are called with methods to move them around the x-y plane and change their speed. 
  the demo program will run by default based off of the commands in main, but one can enter their own commands if they would like. 
  
  
