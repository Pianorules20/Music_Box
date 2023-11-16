#objects.py
import pygame, sys
from pygame.locals import *
import display


class Button():
   
    def __init__(self, description = 'this is my description', number = 'this is my number', \
                  xAxis = 'this is my x length', yAxis = 'this is my y length', \
                    colors = 'these are my colors', border = 'this is my border', pattern = 'this is my pattern'):
        self.description = description
        self.number = number
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.colors = colors
        self.border = border
        self.pattern = pattern
          
    button = pygame.Surface((200, 200), pygame.RESIZABLE)
    
    def BlitNote():
       pass
       

    '''def draw_buttons(x, y):
      for each in Buttons.descriptions:
        layer0 = slice(0)
        layer1 = pygame.font.Font('freesansbold.ttf', 32)
        layer2 = layer1.render(Buttons.descriptions[layer0], True, (10,10,200),(200,170,190))
        layer3 = layer2.get_rect()
        layer3.center = (Buttons.xAxis, Buttons.yAxis)
        splashScreen.Window.screen.blit(layer2, layer3)'''

class Buttons():
  descriptions = []
  xAxis = ()
  yAxis = ()
  def __init__():
     pass
  def populate():
    Play = Button(description = 'press Spacebar to Create and Record', xAxis = 100, yAxis = 100)  
    Buttons.descriptions = (Play.description)
    Buttons.xAxis = (Play.xAxis)
    Buttons.yAxis = (Play.yAxis)

class Note(pygame.sprite.Sprite):

    counter = 0
    #note = pygame.sprite.Sprite()
    note = pygame.Surface((0,0))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen
    
    def __init__(self, frame, x_plot, y_plot) -> None:
        print('Player Object Initiated')
        pygame.sprite.Sprite.__init__(self)
        self.frame = frame
        self.image = pygame.Surface((0,0))
        self.image = pygame.image.load(frame).convert()
        self.rect = self.image.get_rect()
        Note.note = self.image
        self.x_plot = x_plot
        self.y_plot = y_plot
        #Player.face_right = Player.hero
        Note.position = (self.x_plot, self.y_plot)
        display.Window.position= Note.position
        #create.py should handle inputting a new surface into the Window.note position
        Note.rect = self.rect 
    def returnData():
       return Note.note, Note.position
    
    def _blit_():
       display.Window.frame.blit(Note.note, Note.position)
myNotes = []
myPositions = []

'''      Board.Screen.blit(Board.table, (0,0))   # blits basic screen
        Board.Screen.blit(layer2_One, layer3_One)    # blits text Box
        Board.Screen.blit(layer2_Two, layer3_Two)
        Board.Screen.blit(layer2_Three, layer3_Three)
        pygame.event.pump()'''