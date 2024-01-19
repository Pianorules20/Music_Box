#timer.py

import pygame, settings as s

class Data():

    fast = 300
    slow = s.Op.metronome/s.Op.metronomeModifier

    current = fast  