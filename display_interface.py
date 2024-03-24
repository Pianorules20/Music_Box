#display_interface.py
import settings_screen as scn, playback as pb, menu_screen as ms, playback_screen as ps
import settings_screen as o, credits_screen as crs, debug as db, debug_log as dl
import post_production_screen as p_p_s

class Data():
    width = 2000
    height = 1000
    current_screen = 'menu'
    universal_override = False
    override_screen = 'menu'
    currentViewMin = pb.Data.meter
    currentViewMax = pb.Data.meter + 1900

def current(screen):
    match Data.current_screen: 
        case 'menu':
            ms.menu_screen()
        case 'playback':
            ps.playback_screen()
        case 'settings':
            scn.settings_screen()
        case 'credits':
            crs.credits_screen()
        case 'debug':
            db.debug_screen()
        case 'debug log':
            dl.debug_log_screen()
        case 'post_production':
            p_p_s.post_production_screen()

def override(screen):
    match Data.override_screen:
        case 'menu':
            ms.menu_screen()
        case 'playback':
            ps.playback_screen()
        case 'options':
            o.options_screen()
        case 'credits':
            crs.credits_screen()
        case 'debug':
            db.debug_screen()
        case 'debug log':
            dl.debug_log_screen()
        case 'post_production':
            p_p_s.post_production_screen()

def screenGate(screen):
    '''it appears that i need to implement a universal override in order to prevent the screens from changing while the debugging/credits/userinfo /
    is accessed to allow the program to continue so as to allow the logs to continue'''
    if Data.universal_override == True:
        override(screen)
    else:
        current(screen)