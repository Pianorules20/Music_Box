#display_interface.py
import screen_saver as s, playback_meter as pm, menu_screen as ms, playback_screen as ps
import options_screen as o, credits_screen as cs, debug as db

#'I' stands for 'Interface'
class Data():
    width = 2000
    height = 1000
    current = 'menu'
    universal_override = False
    override = 'menu'
    currentViewMin = pm.Meter.meter
    currentViewMax = pm.Meter.meter + 1900


def current(screen):
    match Data.current:
        case 'menu':
            ms.menu_screen()
        case 'playback':
            ps.playback_screen()
        case 'options':
            o.options_screen()
        case 'credits':
            cs.credits_screen()
        case 'debug':
            db.debug_screen()

def override(screen):
    match Data.override:
        case 'menu':
            ms.menu_screen()
        case 'playback':
            ps.playback_screen()
        case 'options':
            o.options_screen()
        case 'credits':
            cs.credits_screen()
        case 'debug':
            db.debug_screen()
 

def screenGate(screen):
    '''it appears that i need to implement a universal override in order to prevent the screens from changing while the debugging/credits/userinfo /
    is accessed to allow the program to continue so as to allow the logs to continue'''
    if Data.universal_override == True:
        override(screen)
    else:
        current(screen)
        

   