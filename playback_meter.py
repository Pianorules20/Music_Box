#playback_meter.py

import settings

class Data():
    
    meter = int(0)

def advance():
    Data.meter += (settings.Data.metronome/settings.Data.metronomeModifier)

def reset_meter():
    Data.meter = int(0)