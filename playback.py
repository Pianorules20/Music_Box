#play.py 
import playback_meter as p_m, gatekeeper as g, timer as t, debug as db, gni #generate_notes_interface
'''import pni as pni, tones as T, gatekeeper as g'''
import pygame, sys
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
    note_count = int(0)
    
def reset_playback():
    Data.note_copy = []
    Data.section_counter = int(0)
    active_notes = []

def advance_playback():
    Data.section_counter += 1
    Data.current_section = Data.note_copy[Data.section_counter]


def play(): #i will play and pop each plot incrementally from the recording
    
    t.Data.current_timer = t.Data.slow
    
    info = f'playback_final_copy_{Data.final_copy}'
    print(info)
    db.Data.debug_log.append(info)
    
    if len(Data.final_copy[0]) > 0:

        for eachNote in Data.final_copy[0]:

            if eachNote.xPos <= p_m.Data.meter:
  
                Sound = gni.Note.returnSound(eachNote) 
                Data.letterName = gni.Note.returnLetterName(eachNote)
                Data.octave = gni.Note.returnOctave(eachNote)
                Data.info = f'Note {Data.letterName}{Data.octave}'
                print(Data.info)
                db.Data.debug_log.append(Data.info)
                #Data.note = tones.Harp.introMusic[eachSound]  
    
                try :
                    
                    pygame.mixer.find_channel(True)
                    pygame.mixer.Sound.play(Sound)
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

                    info = 'playing sound in playback.play()'
                    print(info)
                    db.Data.debug_log.append(info)
                    Data.note_count -= 1

                except Exception as e:
                    info = e
                    print(info)
                    db.Data.debug_log.append(info)
                    crash_me_A = pygame.quit()
                    crash_me_B = sys.exit()
                    crash_me_A
                    crash_me_B
            else:
                pass
            
        p_m.advance()
            #for eachTone in eachIncrement:

    else:
        t.Data.current_timer = t.Data.fast
        p_m.reset_meter()
        g.Data.current_gate = 'post_production'

        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?