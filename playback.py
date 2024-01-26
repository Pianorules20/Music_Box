#play.py 
import playback_meter as pm, gatekeeper as g, timer as t, debug as db, gni #generate_notes_interface
'''import pni as pni, tones as T, gatekeeper as g'''
import pygame
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Data():

    note_copy = [] #this is a list of gni.Note.sound returns
    channel_counter = int(0)
    active_notes = []

def play(): #i will play and pop each plot incrementally from the recording
    
    

    if len(Data.note_copy) > 0:
        
        t.Data.current = t.Data.slow
        print('playing notes')

        for eachNote in Data.note_copy:

            if eachNote.xPos <= pm.Data.meter:
                Data.active_notes.append(eachNote)
                
                the_sound = eachNote.sound

                Data.channel_counter += 1
                if Data.channel_counter >=20:
                    Data.active_notes.pop()
                else:
                    pass

                pygame.mixer.find_channel(True)
            
                
                pygame.mixer.Sound.play(the_sound)

                Data.note_copy.remove(eachNote)

                db.Data.debug_log.append('playing sound in playback.play()')


            else:
                pass
            
            pm.advance()
            #for eachTone in eachIncrement:

            '''T.Tone.play(eachTone)
                print(f'playing {eachTone}')'''

    else:

        g.Data.current = 'post_production'

        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?