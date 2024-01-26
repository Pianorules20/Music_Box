#inputs.py
import pygame, sys, gatekeeper, debug as db, display as d, display_interface as di, text_handler as th
from pygame.locals import *

class Data():
    
    def __init__(self) -> None:
        pass
    

    pygame.event.pump()
    key_press = pygame.key.get_pressed()

        #user_input = pygame.event.get()
    for event in pygame.event.get():
        if key_press[pygame.K_ESCAPE]: 
            info = print("Pause Program")
            db.Data.debug_log.append(info)
            if gatekeeper.Data.current == 'pause':
                pass
            else:
                gatekeeper.Data.saved_place = gatekeeper.Data.current
                gatekeeper.Data.current = 'pause'
        elif key_press[pygame.K_SPACE]:
            if gatekeeper.Data.current == 'pause':
                print('Spacebar Pressed')
                print('continue')
                gatekeeper.Data.current = gatekeeper.Data.saved_place
            else:
                th.Data.scroll_pages == True
                print('th.Data.scroll_pages = True')
                db.Data.debug_log.append('scroll page')
                th.scroll_page()
    

    #for event in pygame.event.get():
    '''match input:
        case pygame.K_SPACE:
            if gatekeeper.Data.current == 'pause':
                print('Spacebar Pressed')
                print('continue')
                gatekeeper.Data.current = gatekeeper.Data.saved_place
            else:
                th.Data.scroll_pages == True
                print('th.Data.scroll_pages = True')
                db.Data.debug_log.append('scroll page')
                th.scroll_page()

        case pygame.K_ESCAPE: 
            db.Data.debug_log.append("Stop playing")
            if gatekeeper.Data.current == 'pause':
                pass
            else:
                gatekeeper.Data.saved_place = gatekeeper.Data.current
                gatekeeper.Data.current = 'pause'

        case pygame.K_RETURN:
            if d.Data.quitting == True:
                db.Data.debug_log.append('Exit Program')
                pygame.quit()
                sys.exit
            else:
                db.Data.debug_log.append(" 'Return' pressed")

        case pygame.K_a:
            db.Data.debug_log.append(" 'A' pressed ")
        case pygame.K_b:
            db.Data.debug_log.append(" 'B' pressed")
        case pygame.K_c:
            db.Data.debug_log.append("'C' pressed")
            if [pygame.K_r]:
                db.Data.debug_log.append('credits accessed')
                if di.Data.universal_override == False:
                    di.Data.universal_override = True
                    di.Data.override = 'credits'
                else:
                    di.Data.universal_override = False
                    di.Data.current = 'menu'
            else:
                pass
        case pygame.K_d:
            db.Data.debug_log.append(" 'D' pressed ")
            if Data.key_press[pygame.K_b]:
                if Data.key_press[pygame.K_g]:
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
        case pygame.K_e:
            db.Data.debug_log.append("'E' pressed")
        case 'f':
            db.Data.debug_log.append("'F' pressed")
        case 'g':
            db.Data.debug_log.append("'G' pressed")
        case 'h':
            db.Data.debug_log.append("'H' pressed")
        case 'i':
            db.Data.debug_log.append("'I' pressed")
        case 'j':
            db.Data.debug_log.append("'J' pressed")
        case 'k':
            db.Data.debug_log.append("'K' pressed")
        case pygame.K_l:
            db.Data.debug_log.append("'L' pressed")
            if Data.key_press[pygame.K_g]:
                db.Data.debug_log.append("'G' pressed")
                db.Data.debug_log.append('debug log accessed')
                if di.Data.universal_override == False:
                    di.Data.universal_override = True
                    di.Data.override = 'debug log'
                else:
                    di.Data.universal_override = False
                    di.Data.current = 'debug'
            else:
                pass
        case pygame.K_m:
            db.Data.debug_log.append(" 'M' pressed")
        case pygame.K_n:
            db.Data.debug_log.append(" 'N' pressed ")
        case pygame.K_o:
            db.Data.debug_log.append(" 'O' pressed ")
        case pygame.K_p:
            db.Data.debug_log.append(" 'P' pressed ")
        case pygame.K_o:
            db.Data.debug_log.append(" 'O' pressed ")
        case pygame.K_p:
            db.Data.debug_log.append(" 'P' pressed ")
        case pygame.K_q:
            db.Data.debug_log.append(" 'Q' pressed ")
            if d.Data.quitting == False:
                d.Data.quitting = True
            else:
                d.Data.quitting = False

        case pygame.K_r:
            db.Data.debug_log.append(" 'R' pressed ")
        case pygame.K_s:
            db.Data.debug_log.append(" 'S' pressed ")
            db.Data.debug_log.append(" settings accessed ")
            if di.Data.universal_override == False:
                di.Data.universal_override = True
                di.Data.override = 'settings'
            else:
                di.Data.universal_override = False
                di.Data.current = 'menu'
        case pygame.K_t:
            db.Data.debug_log.append(" 'T' pressed ")
            if di.Data.universal_override == True:
                if Data.debug_trace == False:
                    db.Data.debug_trace = True
                else:
                    db.Data.debug_trace = False
            else:
                pass   
        case pygame.K_u:
            db.Data.debug_log.append(" 'U' pressed ")
        case pygame.K_v:
            db.Data.debug_log.append(" 'V' pressed ")
        case pygame.K_w:
            db.Data.debug_log.append(" 'W' pressed ")
        case pygame.K_x:
            db.Data.debug_log.append(" 'X' pressed ")
        case pygame.K_y:
            db.Data.debug_log.append(" 'Y' pressed ")
        case pygame.K_z:
            db.Data.debug_log.append(" 'Z' pressed ")'''