#display_interface.py
import settings_screen as scn, playback as pb, menu_screen as ms, playback_screen as ps, credits_screen as crs, debug as db
import post_production_screen as p_p_s

class Data():
    width: int = 2000
    height: int = 1000
    menu: str = 'menu'
    playback: str = 'playback'
    credits: str = 'credits'
    settings: str = 'settings'
    debug: str = 'debug'
    post_production: str = 'post_production'
    
    current_screen: str = 'menu'
    universal_override = False
    override_screen = 'menu'
    currentViewMin = pb.Data.meter
    currentViewMax = pb.Data.meter + 1900

def current(screen):
    match Data.current_screen: 
        case Data.menu:
            ms.menu_screen()
        case Data.playback:
            ps.playback_screen()
        case Data.settings:
            scn.settings_screen()
        case Data.credits:
            crs.credits_screen()
        case Data.debug:
            db.debug_screen()
        case Data.post_production:
            p_p_s.post_production_screen()

def override(screen):
    match Data.current_screen:
        case Data.menu:
            ms.menu_screen()
        case Data.playback:
            ps.playback_screen()
        case Data.settings:
            scn.settings_screen()
        case Data.credits:
            crs.credits_screen()
        case Data.debug:
            db.debug_screen()
        case Data.post_production:
            p_p_s.post_production_screen()

def screenGate(screen):
    '''it appears that i need to implement a universal override in order to prevent the screens from changing while the debugging/credits/userinfo /
    is accessed to allow the program to continue so as to allow the logs to continue'''
    if Data.universal_override == True:
        override(screen)
    else:
        current(screen)