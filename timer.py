#timer.py

import pygame, settings as s

class Timer():

    fast = 300
    slow = s.Op.metronome/s.Op.metronomeModifier

    current = fast  