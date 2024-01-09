#main.py

import pygame
import sys
import objects, display, initializer, introMusic, gatekeeper, timer as t, mySong as my, debug as db

# The term 'motive' is more/less equivalent to 'hook' in the melody of a song.  It is a small piece of pitch and rhythm.
#clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(50)
initializer.Initializer()
objects.Buttons.populate() #this shows the opening screen
print(objects.Buttons.descriptions)
display.Window.updateScreen()
pygame.display.update()
introMusic.play()

#introSound.Intro.loadSounds() #this plays the intro sounds
 #this is necessary so that the motive is populated for the objects in make.Note.play()
class mainLoop():

    def __init__(self) -> None:
        pass
    
    #press SPACEBAR to start program, ESCAPE to stop 
    #the main loop.  a secondary loop exists in play.py 
        #clock.tick(settings.Preferences.pulse) 
        #pygame and pygame.locals controls
    clock  = pygame.time.Clock()
   
    on = True
    
    while on:
        
        #debug only: 
        print(gatekeeper.Gate.current)
        
        clock.tick(t.Timer.current)
        _pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == WINDOWMAXIMIZED:
                print('window maximized')

            if _pressed[pygame.K_SPACE]:
                print('Spacebar Pressed')
                print('continue')
                gatekeeper.Gate.current = gatekeeper.Gate.saved_place
            
            elif _pressed[pygame.K_t]:
                gatekeeper.Gate.testGate()
           
            elif _pressed[pygame.K_ESCAPE]: 
                print("Stop playing")
                if gatekeeper.Gate.current == 'pause':
                    pass
                else:
                    gatekeeper.Gate.saved_place = gatekeeper.Gate.current
                gatekeeper.Gate.current = 'pause'
        
        db.tracer1 = gatekeeper.Gate.current
        db.tracer2 = str(f'currentsection = {my.Trn.currentSection}')
        db.tracer3 = str(f'transcript = {my.Trn.transcript}')
        db.tracer4 = str(f'last trace in ...{db.tracer4}')

        pygame.event.pump()
        display.Window.updateScreen()
        gatekeeper.Gate.passGate(gatekeeper.Gate.current)

pygame.quit()
'''Credits:
    
        The piano samples come from 'www.polyphone-soundfonts.com' user 'JT' on 'Yamaha CFX Studio Grand V2' 
    They were submitted on 11 May, 2020

        The introductory harp originally comes from 'www.freesound.com' by user 'tarane468'.
    I picked it up as a derivative submission at 'www.polyphone-soundfonts.com', which was 
    submitted by user 'Arianna' as 'Celtic Harp.sf2' on 19 February 2017'''