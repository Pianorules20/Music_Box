# plot_meter.py
import settings as s, debug as db

class M():
    
    meter = int(0)

    def advance():
        M.meter += s.Preferences.metronome
        db.Data.debug_log.append('advancing meter = {M.meter}')

    def reset():
        M.meter = int(0)