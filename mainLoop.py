#main.py

import pygame
import sys
import display as d, initializer as init, introMusic, gatekeeper as g, timer as t
import display_interface as di, screen_saver as ss, layout_menu_style as lm, layout_playback_style as lp
import text_handler as th, debug as db, fonts as f

# The term 'motive' is more/less equivalent to 'hook' in the melody of a song.  It is a small piece of pitch and rhythm.
#clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(50)
lm.Data()
lp.Data()
init.initialize()
#objects.Buttons.populate() #this shows the opening screen
#print(objects.Buttons.descriptions)
d.Data.updateScreen()
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

    '''class Data():
        pass'''
    
    while on:

        clock.tick(t.Data.current_timer)
        '''clock_titleA = "clock speed"
        clock_titleB = f.Data.scripted
        clock_titleC = clock_titleB.render(clock_titleA, True, ss.Data.text, ss.Data.rbg)
        clock_titleD = clock_titleC.get_rect()
        clock_titleD.bottomleft = (lm.Data.x10, lm.Data.x100)
        #blitted on 'debug_page_2'
        clock_currentA = str(t.Data.current_timer)
        clock_currentB = f.Data.subtitle
        clock_currentC = clock_currentB.render(clock_currentA, True, ss.Data.text, ss.Data.rbg)
        clock_currentD = clock_titleC.get_rect()
        clock_currentD'''

        key_press = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            elif event.type == WINDOWMAXIMIZED:
                print('window maximized')


            if  key_press[pygame.K_SPACE]:
                info = 'Spacebar Pressed'
                db.Data.debug_log.append(info)
                if g.Data.current_gate == 'pause':
                    g.Data.current_gate = g.Data.saved_place
                else:
                    info = 'th.Data.scroll_pages = True'
                    print(info)
                    db.Data.debug_log.append(info)
                    th.Data.scroll_pages == True 
                    th.scroll_page()
            elif key_press[pygame.K_ESCAPE]: 
                info = "Pause program"
                print(info)
                #db.Data.debug_log.append(info)
                if g.Data.current_gate == 'pause':
                    pass
                else:
                    g.Data.saved_place = g.Data.current_gate
                    g.Data.current_gate = 'pause'
            elif key_press[pygame.K_RETURN]:
                info = "RETURN pressed"
                print(info)
                db.Data.debug_log.append(info)
                if d.Data.quitting == True:
                    db.Data.debug_log.append('Exit Program')
                    pygame.quit()
                    sys.exit
                else:
                        pass
                
            elif key_press[pygame.K_c]:
                info = " 'C' pressed "
                print(info)
                db.Data.debug_log.append(info)
                if key_press[pygame.K_r]:
                    info = " Credits accessed "
                    print(info)
                    db.Data.debug_log.append(info)
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override_screen = 'credits'
                    else:
                        di.Data.universal_override = False
                        di.Data.current_screen = 'menu'
                else:
                    pass
            elif key_press[pygame.K_d]:
                info = " 'B' pressed "
                print(info)
                db.Data.debug_log.append(info)
                if key_press[pygame.K_d]:
                    info = " D pressed "
                    print(info)
                    db.Data.debug_log.append(info)
                    #db.Data.debug_log.append(info)
                    #if key_press[pygame.K_g]:
                        #info = print("Debug accessed")
                        #db.Data.debug_log.append(info)
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override_screen = 'debug'
                    else:
                        di.Data.universal_override = False
                        di.Data.current_screen = 'menu'
                else:                        
                    pass
            
            elif key_press[pygame.K_l]:
                info = " 'L' pressed "
                print(info)
                db.Data.debug_log.append(info)
                if key_press[pygame.K_g]:
                    info = 'debug log accessed'
                    print(info)
                    db.Data.debug_log.append(info)
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override_screen = 'debug log'
                    else:
                        di.Data.universal_override = False
                        di.Data.current_screen = 'debug'
                else:
                    pass
              
            elif key_press[pygame.K_q]:
                info = " 'Q' pressed "
                print(info)
                db.Data.debug_log.append(info)
                if d.Data.quitting == False:
                    d.Data.quitting = True
                else:
                    d.Data.quitting = False
                
            elif key_press[pygame.K_s]:
                info = " 'S' pressed "
                print(info)
                db.Data.debug_log.append(info)
                db.Data.debug_log.append("_settings_accessed_")
                if di.Data.universal_override == False:
                    di.Data.universal_override = True
                    di.Data.override_screen = 'settings'
                else:
                    di.Data.universal_override = False
                    di.Data.current_screen = 'menu'
            elif key_press[pygame.K_t]:
                info = " 'T' pressed "
                print(info)
                db.Data.debug_log.append(info)
                if di.Data.universal_override == True:
                    if db.Data.debug_trace == False:
                        db.Data.debug_trace = True
                    else:
                        db.Data.debug_trace = False
                else:
                    pass   
        ss.advance()
        pygame.event.pump() 
        d.Data.updateScreen()
        g.passGate(g.Data.current_gate)

pygame.quit()
'''Credits:
    
        The piano samples come from 'www.polyphone-soundfonts.com' user 'JT' on 'Yamaha CFX Studio Grand V2' 
    They were submitted on 11 May, 2020
 
        The introductory harp originally comes from 'www.freesound.com' by user 'tarane468'.
    I picked it up as a derivative submission at 'www.polyphone-soundfonts.com', which was 
    submitted by user 'Arianna' as 'Celtic Harp.sf2' on 19 February 2017'''