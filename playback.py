#play.py 
import mySong, generate_notes_interface, playbackMeter, settings, pygame, gatekeeper, timer as t
import plot_notes_interface as pni
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Player():

    recording = []

    def play():

        t.Timer.current = t.Timer.slow
        
        for eachPlot in Player.recording:

                pni.P.play(eachPlot)
        
        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?