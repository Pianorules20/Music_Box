#timer.py

import pygame, settings as s

class Data():

    fast = 300
    slow = s.Data.metronome/s.Data.metronomeModifier

    current_timer = fast