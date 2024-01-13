#main.py

import pygame
import sys
import objects, display, initializer, introMusic, gatekeeper, timer as t, mySong as my, debug as db
import display_interface as di, screen_saver as ss, layout_menu_style as lm, layout_playback_style as lp

# The term 'motive' is more/less equivalent to 'hook' in the melody of a song.  It is a small piece of pitch and rhythm.
#clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(50)
lm.initialize()
lp.initialize()
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
        
        clock.tick(t.Data.current)
        _pressed = pygame.key.get_pressed() #keyboard controls 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == WINDOWMAXIMIZED:
                print('window maximized')

            if _pressed[pygame.K_SPACE]:
                print('Spacebar Pressed')
                print('continue')
                gatekeeper.Data.current = gatekeeper.Data.saved_place
            
            elif _pressed[pygame.K_d]:
                if _pressed[pygame.K_b]:
                    if _pressed[pygame.K_g]:
                        db.Data.debug_log.append('debug accessed')
                        if di.Data.universal_override == False:
                            di.Data.universal_override = True
                            di.Data.override = 'debug'
                        else:
                            di.Data.universal_override = False
                            di.Data.current = 'menu'
                    else:
                        pass
                else:
                    pass

            elif _pressed[pygame.K_c]:
                db.Data.debug_log.append("'C' pressed")
                if _pressed[pygame.K_r]:
                    db.Data.debug_log.append('credits accessed')
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override = 'credits'
                    else:
                        di.Data.universal_override = False
                        di.Data.current = 'menu'
                else:
                    pass

            elif _pressed[pygame.K_r]:
                db.Data.debug_log.append("'R' pressed")

            elif _pressed[pygame.K_e]:
                db.Data.debug_log.append("'E' pressed")

            elif _pressed[pygame.K_t]:
                if di.Data.universal_override == True:
                    if db.Data.debug_trace == False:
                        db.Data.debug_trace = True
                        db.Data.debug_log.append('trace path')
                    else:
                        db.Data.debug_trace = False
                else:
                    pass
           
            elif _pressed[pygame.K_ESCAPE]: 
                db.Data.debug_log.append("Stop playing")
                if gatekeeper.Data.current == 'pause':
                    pass
                else:
                    gatekeeper.Data.saved_place = gatekeeper.Data.current
                gatekeeper.Data.current = 'pause'

        ss.advance()
        pygame.event.pump()
        display.Window.updateScreen()
        gatekeeper.passGate(gatekeeper.Data.current)

pygame.quit()
'''Credits:
    
        The piano samples come from 'www.polyphone-soundfonts.com' user 'JT' on 'Yamaha CFX Studio Grand V2' 
    They were submitted on 11 May, 2020
 
        The introductory harp originally comes from 'www.freesound.com' by user 'tarane468'.
    I picked it up as a derivative submission at 'www.polyphone-soundfonts.com', which was 
    submitted by user 'Arianna' as 'Celtic Harp.sf2' on 19 February 2017'''