import pygame
from enum import Enum
import random
from entity import *

pygame.init()

# Some Global Config
RECT_TILE_WIDTH_COUNT = RECT_TILE_HEIGHT_COUNT = 8
RECT_WIDTH_PIXEL = RECT_HEIGHT_PIXEL = 4

class Color(Enum):
    WHITE = [255, 255, 255]
    
    GRASS_GREEN = [155, 255, 90]
    GRASS_GREEN_SHADE = [74, 115, 47]

    ROCK_GRAY = [190, 190, 190]
    ROCK_GRAY_SHADE = [133, 124, 124]

    RIVER_BLUE = [113, 205, 255]
    RIVER_BLUE_SHADE = [82, 167, 213]

class TileColor(Enum):
    GRASS_TEST = [(Color.GRASS_GREEN if random.random() < 0.2 else Color.GRASS_GREEN_SHADE) for i in range(RECT_TILE_WIDTH_COUNT*RECT_TILE_HEIGHT_COUNT)]
    ROCK_TEST = [(Color.ROCK_GRAY if random.random() < 0.7 else Color.ROCK_GRAY_SHADE) for i in range(RECT_TILE_WIDTH_COUNT*RECT_TILE_HEIGHT_COUNT)]
    RIVER_TEST = [(Color.RIVER_BLUE if random.random() < 0.9 else Color.RIVER_BLUE_SHADE) for i in range(RECT_TILE_WIDTH_COUNT*RECT_TILE_HEIGHT_COUNT)]


    # tool needed a tile builder ???

class DisplayTool:
    """
    Class contains needed functionality for display the game
    """
    def __init__(self, display):
        self.display = display
        self.circleRadius = 1
        self.circleWidth = 0 # 0 fill, >0: thickness, <0 nothing will be drawn
        
        self.rectWidth = RECT_WIDTH_PIXEL; # pixel Width 

        self.rectTileWidthCount = RECT_TILE_WIDTH_COUNT; # how many pixel in a tile width

        self.rectTotalPixelTile = self.rectWidth * self.rectTileWidthCount # keep it the same for now
        
        self.colorMapping = {
            'tree': TileColor.GRASS_TEST,
            'rock': TileColor.ROCK_TEST,
            'river': TileColor.RIVER_TEST
        }

    def drawPixel(self, pos, color, op='r'): 
        """
        pos: [int, int]
        color: [int, int ,int]
        """
        if op == 'c':
            pygame.draw.circle(self.display, color, pos, self.circleRadius, self.circleWidth)
        elif op == 'r':
            pygame.draw.rect(self.display, color, [pos[0], pos[1], self.rectWidth, self.rectWidth])
    
    def drawTile(self, tile):
        """
        tile pos is top left
        0    1     2     3    4    5    6    7
        8    9    10    11    12    13    14    15
        ...

        """
        tileColor = self.colorMapping[tile.env] # modified tileColor
        for i in range(0, len(tileColor.value)):
            pos = [0, 0]
            # pos =	pos within map * size 				+ inner pos of color
            pos[0] = tile.x*self.rectTotalPixelTile 	+ (i%self.rectTileWidthCount) * self.rectWidth
            pos[1] = tile.y*self.rectTotalPixelTile    + int(i/self.rectTileWidthCount) * self.rectWidth
            self.drawPixel(pos, tileColor.value[i].value)

    def drawMap(self, list_map, player):
        #for i in range(player.pos)
        """
        list_map is 2d array contain x row of tile
        """
        for j in range(len(list_map)):
            for i in range(len(list_map[j])):
                tile = list_map[j][i]
                # need to check if within render distance
                # need to change coordinate to display coordinate
                self.drawTile(tile)
                
                
        pass



# Initialize display 
gameDisplay = pygame.display.set_mode((800,600))
displayTool = DisplayTool(gameDisplay)

# Initialize entity
MAX_X = 20
MAX_Y = 20
map_1 = Map(MAX_X, MAX_Y)
print(map_1.createRandomEnvMap())

player = Player(10,10)

pygame.display.set_caption('Just A Game')

clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            print([event.pos, event.button])
            print(Color.WHITE)
            #displayTool.drawPixel(event.pos, Color.WHITE.value, 'r')
            map_1.createRandomEnvMap()
            displayTool.drawMap(map_1.list_map, player)
        print([event.type, event])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
