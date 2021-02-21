# for entity set up
 import random 
envionment_list = ['tree', 'rock', 'river']

class Titles:

    def __init__(self, max_x, max_y):
        if not isinstance(max_x, int):
            raise TypeError('x must be integer')
        if not isinstance(max_y, int):
            raise TypeError('y must be integer')
        list_map = []

        y = 0
        while y < max_y:
            x = 0
            while x < max_x:
                list_map.append([x, y, random.choice(envionment_list)])
                x +=1
            list_map.append([x, y, random.choice(envionment_list)])
            y +=1
        
        self.list_map = list_map
        
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

Player(8, 9).return_position()
