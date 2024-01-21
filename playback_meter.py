#recordMeter.py
import settings

class Data():
    
    meter = int(0)

def advance():
    Data.meter += (settings.Data.metronome/settings.Preferences.metronomeModifier)

def reset():
    Data.meter = int(0)