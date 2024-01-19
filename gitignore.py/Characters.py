# Characters.py
import pygame, sys
from pygame.locals import *
import Display
import time

class Player(pygame.sprite.Sprite):

    counter = 0
    
    hero = pygame.sprite.Sprite()
    hero = pygame.Surface((0,0))

    rect = ()
    position = ()
    face_right = pygame.Surface((0,0))
    face_left = pygame.Surface((0,0))
    facing = 'right'
    
    def __init__(self, frame) -> None:
        print('Player Object Initiated')
        pygame.sprite.Sprite.__init__(self)
        self.frame = frame
        self.image = pygame.Surface((0,0))
        self.image = pygame.image.load(frame).convert()
        self.rect = self.image.get_rect()
        Player.hero = self.image
        Player.face_right = Player.hero
        Player.position = (Display.Window.width/2, Display.Window.height/2)
        Display.Window.position= Player.position
        Display.Window.hero = Player.hero
        Player.rect = self.rect 
        Player.face_left =  pygame.transform.flip(Player.face_right, True, False)

    def updateFrame(direction, vector):
            
        clock = pygame.time.Clock()

        if direction == 'left':
            Player.facing = 'left'
            Player.hero = Player.face_left 
            Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            Display.Window.updateScreen()
            pygame.display.update()    
        if direction == 'right':
            Player.facing = 'right'
            Player.hero = Player.face_right
            Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            Display.Window.updateScreen()
            pygame.display.update()  
        if direction == 'up':
        
            Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            Display.Window.updateScreen()
            pygame.display.update()
        if direction == 'down':

            Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            Display.Window.updateScreen()
            pygame.display.update()
        if direction == 'jump':  
            
            for i in range(25):
               
                if Player.facing == 'right':
                    Player.position = (Player.position[0]+vector[0]*4, Player.position[1]+vector[1]*4)    

                elif Player.facing == 'left':
                    Player.position = (Player.position[0]-vector[0]*4, Player.position[1]+vector[1]*4)
                
                Display.Window.updateScreen()
                pygame.display.update()
                

        if direction == 'land':
            for i in range(25):

                if Player.facing == 'right':
                    Player.position = Player.position[0]+vector[0]*4, Player.position[1]+vector[1]*4
                
                elif Player.facing == 'left':    
                    Player.position = (Player.position[0]-vector[0]*4, Player.position[1]+vector[1]*4)
                
                Display.Window.updateScreen()
                pygame.display.update()

        if direction == 'fly':
            for i in range(25):
               
                if Player.facing == 'right':
                    Player.position = (Player.position[0]+vector[0]*4, Player.position[1]+vector[1]*4)    

                elif Player.facing == 'left':
                    Player.position = (Player.position[0]-vector[0]*4, Player.position[1]+vector[1]*4)
               
                Display.Window.updateScreen()
                pygame.display.update()
        
        if direction == 'attack':
            Player.hero = pygame.image.load('sprites/characters/attack1.png').convert() 
            
            if Player.facing == 'right':

                Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
                   
            elif Player.facing == 'left':
                Player.face_left =  pygame.transform.flip(Player.face_right, True, False)
                Player.position = (Player.position[0]-vector[0], Player.position[1]+vector[1])

            Display.Window.updateScreen()
            pygame.display.update()

            Player.hero = pygame.image.load('sprites/characters/attack2.png').convert() 

            if Player.facing == 'right':
                Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            
            elif Player.facing == 'left':
                Player.face_left = pygame.transform.flip(Player.face_right, True, False)
                Player.position = (Player.position[0]-vector[0], Player.position[1]+vector[1])
            
            Display.Window.updateScreen()
            pygame.display.update()

            Player.hero = pygame.image.load('sprites/characters/attack3.png').convert()

            if Player.facing == 'right':
                Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            
            elif Player.facing == 'left':
                Player.face_left = pygame.transform.flip(Player.face_right, True, False)
                Player.position = (Player.position[0]-vector[0], Player.position[1]+vector[1])
            Display.Window.updateScreen()
            pygame.display.update()

            Player.hero = pygame.image.load('sprites/characters/attack4.png').convert()

            if Player.facing == 'right':
                Player.position = (Player.position[0]+vector[0], Player.position[1]+vector[1])
            
            elif Player.facing == 'left':
                Player.face_left = pygame.transform.flip(Player.face_right, True, False)
                Player.position = (Player.position[0]-vector[0], Player.position[1]+vector[1])
            Display.Window.updateScreen()
            pygame.display.update()

SuperSpriteEx = Player('sprites/characters/mannys_run1.png')
