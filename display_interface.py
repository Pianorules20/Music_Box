#display_interface.py
import screens, playbackMeter

class Interface():

    current = 'menu'
    currentViewMax = playbackMeter.Meter.meter + 1900
    currentViewMin = playbackMeter.Meter.meter

    def screenGate(screen):
        
        match screen:     
            case 'menu':
                branch = screens.Screens.menu()
            case 'player':
                branch = screens.Screens.player()
            case 'options':
                branch = screens.Screens.options()    
        return branch