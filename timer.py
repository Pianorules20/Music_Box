#timer.py

import settings as s

class Data():

    fast = 320
    slow = float(s.Data.metronome * 0.1 / s.Data.metronomeModifier)

    current = fast