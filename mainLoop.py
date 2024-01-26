#main.py

import pygame
import sys
import objects, display as d, initializer as init, introMusic, gatekeeper as g, timer as t
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
objects.Buttons.populate() #this shows the opening screen
print(objects.Buttons.descriptions)
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

        clock.tick(t.Data.current)
        clock_titleA = "clock speed"
        clock_titleB = f.Data.scripted
        clock_titleC = clock_titleB.render(clock_titleA, True, ss.Data.text, ss.Data.rbg)
        clock_titleD = clock_titleC.get_rect()
        clock_titleD.bottomleft = (lm.Data.x10, lm.Data.x100)
        #blitted on 'debug_page_2'
        clock_currentA = str(t.Data.current)
        clock_currentB = f.Data.subtitle
        clock_currentC = clock_currentB.render(clock_currentA, True, ss.Data.text, ss.Data.rbg)
        clock_currentD = clock_titleC.get_rect()
        clock_currentD

        key_press = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            elif event.type == WINDOWMAXIMIZED:
                print('window maximized')


            if  key_press[pygame.K_SPACE]:
                info = print('Spacebar Pressed')
                db.Data.debug_log.append(info)
                if g.Data.current == 'pause':
                    g.Data.current = g.Data.saved_place
                else:
                    info = print('th.Data.scroll_pages = True')
                    db.Data.debug_log.append(info)
                    th.Data.scroll_pages == True 
                    th.scroll_page()
            elif key_press[pygame.K_ESCAPE]: 
                info = print("Pause program")
                db.Data.debug_log.append(info)
                if g.Data.current == 'pause':
                    pass
                else:
                    g.Data.saved_place = g.Data.current
                    g.Data.current = 'pause'
            elif key_press[pygame.K_RETURN]:
                info = print("RETURN pressed")
                db.Data.debug_log.append(info)
                if d.Data.quitting == True:
                    db.Data.debug_log.append('Exit Program')
                    pygame.quit()
                    sys.exit
                else:
                        pass
            
            elif key_press[pygame.K_a]:
                info = print(" 'A' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_b]:
                info = print(" 'B' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_c]:
                info = print(" 'C' pressed ")
                db.Data.debug_log.append(info)
                if key_press[pygame.K_r]:
                    info = print(" Credits accessed ")
                    db.Data.debug_log.append(info)
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override = 'credits'
                    else:
                        di.Data.universal_override = False
                        di.Data.current = 'menu'
                else:
                    pass
            elif key_press[pygame.K_d]:
                info = print(" 'B' pressed ")
                db.Data.debug_log.append(info)
                if key_press[pygame.K_d]:
                    info = print(" D pressed ")
                    #db.Data.debug_log.append(info)
                    #if key_press[pygame.K_g]:
                        #info = print("Debug accessed")
                        #db.Data.debug_log.append(info)
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override = 'debug'
                    else:
                        di.Data.universal_override = False
                        di.Data.current = 'menu'
                else:                        
                    pass
                #else:
                #    pass
            elif key_press[pygame.K_e]:
                info = print(" 'E' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_f]:
                info = print(" 'F' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_g]:
                info = print(" 'G' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_h]:
                info = print(" 'H' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_i]:
                info = print(" 'I' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_j]:
                info = print(" 'J' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_k]:
                info = print(" 'K' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_l]:
                info = print(" 'L' pressed ")
                #db.Data.debug_log.append(info)
                if key_press[pygame.K_g]:
                    #info = print('debug log accessed')
                    #db.Data.debug_log.append(info)
                    if di.Data.universal_override == False:
                        di.Data.universal_override = True
                        di.Data.override = 'debug log'
                    else:
                        di.Data.universal_override = False
                        di.Data.current = 'debug'
                else:
                    pass
            elif key_press[pygame.K_m]:
                info = print(" 'M' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_n]:
                info = print(" 'N' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_o]:
                info = print(" 'O' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_p]:
                info = print(" 'P' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_q]:
                info = print(" 'Q' pressed ")
                db.Data.debug_log.append(info)
                if d.Data.quitting == False:
                    d.Data.quitting = True
                else:
                    d.Data.quitting = False
            elif key_press[pygame.K_r]:
                info = print(" 'R' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_s]:
                info = print(" 'S' pressed ")
                db.Data.debug_log.append(info)
                db.Data.debug_log.append(" settings accessed ")
                if di.Data.universal_override == False:
                    di.Data.universal_override = True
                    di.Data.override = 'settings'
                else:
                    di.Data.universal_override = False
                    di.Data.current = 'menu'
            elif key_press[pygame.K_t]:
                info = print(" 'T' pressed ")
                db.Data.debug_log.append(info)
                if di.Data.universal_override == True:
                    if db.Data.debug_trace == False:
                        db.Data.debug_trace = True
                    else:
                        db.Data.debug_trace = False
                else:
                    pass   
            elif key_press[pygame.K_u]:
                info = print(" 'U' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_v]:
                info = print(" 'V' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_w]:
                info = print(" 'w' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_x]:
                info = print(" 'X' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_y]:
                info = print(" 'Y' pressed ")
                db.Data.debug_log.append(info)
            elif key_press[pygame.K_z]:
                info = print(" 'Z' pressed ")
                db.Data.debug_log.append(info)
            #inp.keyboard_inputs()
                
        ss.advance()
        pygame.event.pump() 
        d.Data.updateScreen()
        g.passGate(g.Data.current)

pygame.quit()
'''Credits:
    
        The piano samples come from 'www.polyphone-soundfonts.com' user 'JT' on 'Yamaha CFX Studio Grand V2' 
    They were submitted on 11 May, 2020
 
        The introductory harp originally comes from 'www.freesound.com' by user 'tarane468'.
    I picked it up as a derivative submission at 'www.polyphone-soundfonts.com', which was 
    submitted by user 'Arianna' as 'Celtic Harp.sf2' on 19 February 2017'''