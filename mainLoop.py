#mainLoop.py

import pygame
import sys
import display as d, populate_instance as p_i, introMusic, gatekeeper as g, timer as t, debug as db
import display_interface as d_i, screen_saver as s_s, layout_menu_style as lm, layout_playback_style as lp
# The term 'motive' is more/less equivalent to 'hook' in the melody of a song.  It is a small piece of pitch and rhythm.
#clock = pygame.time.Clock()
from pygame.locals import *
pygame.mixer.init()
pygame.mixer.set_num_channels(1000)
pygame.init()
lm.Data()
lp.Data()
p_i.initialize()
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

        clock.tick(t.Data.current)
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
                info = str('Spacebar Pressed')
                db.Data.debug_log = info
                if g.Data.current_gate == g.Data.pause:
                    g.Data.current_gate = g.Data.saved_place
                else:
                    info = 'th.Data.scroll_pages = True'
                    print(info)
                    #db.Data.debug_log.append(info)
                    #th.Data.scroll_pages == True 
                    #th.scroll_page()
            elif key_press[pygame.K_ESCAPE]: 
                info = "Pause program"
                print(info)
                #db.Data.debug_log.append(info)
                if g.Data.current_gate == g.Data.pause:
                    pass
                else:
                    g.Data.saved_place = g.Data.current_gate
                    g.Data.current_gate = g.Data.pause
            elif key_press[pygame.K_RETURN]:
                info = str("RETURN pressed")
                print(info)
                #db.Data.debug_log.append(info)
                if d.Data.quitting == True:
                    #db.Data.debug_log.append('Exit Program')
                    pygame.quit()
                    sys.exit
                else:
                        pass
                
            elif key_press[pygame.K_c]:
                info = " 'C' pressed "
                print(info)
                #db.Data.debug_log.append(info)
                if key_press[pygame.K_r]:
                    info = " Credits accessed "
                    print(info)
                    #db.Data.debug_log.append(info)
                    if d_i.Data.universal_override == False:
                        d_i.Data.universal_override = True
                        d_i.Data.override_screen = d_i.Data.credits
                    else:
                        d_i.Data.universal_override = False
                        d_i.Data.current_screen = d_i.Data.menu
                else:
                    pass
            elif key_press[pygame.K_d]:
                info = " 'D' pressed "
                print(info)
                #db.Data.debug_log.append(info)
                if key_press[pygame.K_b]:
                    info = " B pressed "
                    print(info)
                    #db.Data.debug_log.append(info)
                    if key_press[pygame.K_g]:
                        info = print("Debug accessed")
                        print(info)
                        #db.Data.debug_log.append(info)
                        if d_i.Data.universal_override == False:
                            d_i.Data.universal_override = True
                            d_i.Data.override_screen = d_i.Data.debug
                        else:
                            d_i.Data.universal_override = False
                            d_i.Data.current_screen = d_i.Data.debug
                    else:
                        pass
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
                    if d_i.Data.universal_override == False:
                        d_i.Data.universal_override = True
                        d_i.Data.override_screen = d_i.Data.debug_log
                    else:
                        d_i.Data.universal_override = False
                        d_i.Data.current_screen = d_i.Data.debug
                else:
                    pass
            elif key_press[pygame.K_q]:
                info = " 'Q' pressed "
                print(info)
                #db.Data.debug_log.append(info)
                if d.Data.quitting == False:
                    d.Data.quitting = True
                else:
                    d.Data.quitting = False
                
            elif key_press[pygame.K_s]:
                info = " 'S' pressed "
                print(info)
                #db.Data.debug_log.append(info)
                #db.Data.debug_log.append("_settings_accessed_")
                if d_i.Data.universal_override == False:
                    d_i.Data.universal_override = True
                    d_i.Data.override_screen = d_i.Data.settings
                else:
                    d_i.Data.universal_override = False
                    d_i.Data.current_screen = d_i.Data.menu
            elif key_press[pygame.K_t]:
                info = " 'T' pressed "
                print(info)
                #db.Data.debug_log.append(info)
                if d_i.Data.universal_override == True:
                    if db.Data.debug_trace == False:
                        db.Data.debug_trace = True
                    else:
                        db.Data.debug_trace = False
                else:
                    pass   
        s_s.advance()
        pygame.event.pump() 
        d.Data.updateScreen()
        print(f'current_gate = {g.Data.current_gate} ')
        info = f'clock speed = {t.Data.current}'
        print(info)
        #info = f'settings.Data.structure = {s.Data.structure}'
        #print(info)
        #debug_log_count = len(db.Data.debug_log)
        #print(debug_log_count)
        #d_f.magnify('pni.Plot.sounds', pni.Plot.sounds)
        g.passGate(g.Data.current_gate)


pygame.quit()
