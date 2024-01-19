#play.py 
import playback_meter as pm, gatekeeper as g, timer as t, tones as T
'''import pni as pni, tones as T, gatekeeper as g'''
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Data():

    recording = []

def play(): #i will play and pop each plot incrementally from the recording
    
    if len(Data.recording) > 0:
       
        print('playing notes')

        for eachPlot in Data.recording:
            t.Data.current = t.Data.slow
            eachPlot.playNotes()
            #for eachTone in eachIncrement:

            '''T.Tone.play(eachTone)
                print(f'playing {eachTone}')'''

    else:

        g.Gate.current = 'post_production'

        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?