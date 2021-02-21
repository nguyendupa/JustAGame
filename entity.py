# for entity set up
import random 
envionment_list = ['tree', 'rock', 'river']

class Tile:
    def __init__(self, x, y, env):
        self.x = x
        self.y = y
        self.env = env

    #need to double check
    def isWithinRenderDistance(self):
        pass

class Map:

    def __init__(self, size_x, size_y):
        if not isinstance(size_x, int):
            raise TypeError('x must be integer')
        if not isinstance(size_y, int):
            raise TypeError('y must be integer')
        self.size_x = size_x
        self.size_y = size_y
        self.list_map = []

    def createRandomEnvMap(self):
        list_map = []

        for y in range(self.size_y):
            list_map.append([])
            for x in range(self.size_x):
                list_map[y].append( Tile(x, y, random.choice(envionment_list) ) )                  
        self.list_map = list_map

        return self.list_map
        
class Player:
    
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError('x must be integer')
        if not isinstance(y, int):
            raise TypeError('y must be integer')
        
        self.x = x
        self.y = y

    def return_position(self):    
        return([self.x, self.y])

