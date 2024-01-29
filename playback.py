#play.py 
import playback_meter as pm, gatekeeper as g, timer as t, debug as db, gni #generate_notes_interface
'''import pni as pni, tones as T, gatekeeper as g'''
import pygame
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Data():

    transfer_notes = True    
    final_copy = [] #this is a list of gni.Note.sound returns
    section_counter = int(0)
    current_section = []
    channel_counter = int(0)
    active_notes = []
    
def reset_playback():
    Data.note_copy = []
    Data.section_counter = int(0)
    active_notes = []

def advance_playback():
    Data.section_counter += 1
    Data.current_section = Data.note_copy[Data.section_counter]


def play(): #i will play and pop each plot incrementally from the recording
    
    t.Data.current = t.Data.slow
    if len(Data.final_copy[0]) > 0:
        
        print('playing notes')

        for eachNote in Data.final_copy[0]:

            if eachNote.xPos <= pm.Data.meter:
                #Data.active_notes.append(eachNote)
                
                the_sound = eachNote.sound

                #Data.channel_counter += 1
                #if Data.channel_counter >=20:
                    #Data.active_notes.pop()
                #else:
                #    pass

                pygame.mixer.find_channel(True)
            
                pygame.mixer.Sound.play(the_sound)

                Data.final_copy[0].remove(eachNote)

                db.Data.debug_log.append('playing sound in playback.play()')

                
            else:
                pass
            
        pm.advance()
            #for eachTone in eachIncrement:

    else:

        pm.reset_meter()
        g.Data.current = 'post_production'

        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?