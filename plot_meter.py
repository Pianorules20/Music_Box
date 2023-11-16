# plot_meter.py
import settings as s

class M():
    
    meter = int(0)

    def advance():
        M.meter += s.Preferences.metronome

    def reset():
        M.meter = int(0)