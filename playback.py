#play.py 
import playback_meter as pm, settings, pygame, gatekeeper as g, timer as t, tones as T
'''import pni as pni, tones as T, gatekeeper as g'''
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Player():

    recording = []

def play(): #i will play and pop each plot incrementally from the recording
    
    if len(Player.recording) > 0:
       
        print('playing notes')
    
        t.Data.current = t.Data.slow

        for eachPlot in Player.recording:

            eachPlot.playNotes()
            #for eachTone in eachIncrement:

            '''T.Tone.play(eachTone)
                print(f'playing {eachTone}')'''

    else:

        g.Gate.current = 'post_production'

        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?