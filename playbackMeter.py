#recordMeter.py
import settings

class Meter():
    
    meter = int(0)


    def advance():
        Meter.meter += (settings.Preferences.metronome/settings.Preferences.metronomeModifier)

    def reset():
        Meter.meter = int(0)
