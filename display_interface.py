#display_interface.py
import screens as s, playback_meter as pm

class I(): #'I' stands for 'Interface'

    width = 2000
    height = 1200
    current = 'menu'
    currentViewMin = pm.Meter.meter
    currentViewMax = pm.Meter.meter + 1900

    def screenGate(screen):
        
        match screen:     
            case 'menu':
                s.Screens.menu()
            case 'player':
                s.Screens.player()
            case 'options':
                s.Screens.options()   
            case 'credits':
                s.Screens.credits()