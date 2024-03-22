#playback.py 
import gatekeeper as g, timer as t, debug as db, state, gni #generate_notes_interface
import pygame, sys, my_song as m_s, settings as s, display_interface as d_i, tones
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Data():
    
    final_copy = [] #this is a list of the plots including null plots
    current_plot = []
    current_section = []

    transfer_notes = True    
    section_counter = int(0)
    
    channel_counter = int(0)
    #active_notes = []
    note_count = int(0)
    meter = int(0)
    plot_meter_saved = int(0)
    ranger = int(0)

'''def advance():
    Data.meter += (s.Data.metronome/s.Data.metronomeModifier)'''
def advance():
    Data.meter += 1

def reset_meter():
    Data.meter = int(0)
    
def reset_playback():
    Data.final_copy = []
    Data.section_counter = int(0)
    Data.transfer_notes = not Data.transfer_notes
    #active_notes = []

def advance_playback():
    Data.section_counter += 1
    Data.current_section = Data.final_copy[Data.section_counter]

def play(): #i will play and pop each plot incrementally from the recording
    
    '''info = f'in playback note_count {Data.note_count}' 
    print(info) # breadcrumb
    db.Data.debug_log = info'''

    
    if Data.section_counter > 1:
        Data.current_section = Data.final_copy[Data.section_counter]
        Data.current_plot = Data.current_section[Data.meter]
    else:
        Data.current_plot = Data.final_copy[Data.meter]

    info = f'in playback, Data.current_plot = {Data.current_plot} '
    print(info)
    db.Data.debug_log = info
    
    t.Data.current_timer = t.Data.slow
    
    #info = f'playback_final_copy_{Data.final_copy}'
    #print(info)
    #db.Data.debug_log = info
    
    if Data.meter < Data.plot_meter_saved:

        Data.ranger = len(Data.current_plot)
        for eachInteger in range(Data.ranger):
            tones.Tone.play(Data.current_plot[eachInteger])
        #Sound = gni.Note.returnSound(eachNote) 
        #Data.letterName = gni.Note.returnLetterName(eachNote)
        #Data.octave = gni.Note.returnOctave(eachNote)
        #info = f'Note {eachNote.letterName}{eachNote.octave}'
        #print(info)
        #db.Data.debug_log.append(info)
        #Data.note = tones.Harp.introMusic[eachSound]  
    
        '''try :
                    
                    gni.Note.play(eachNote.sound)

                    #pygame.mixer.find_channel(True)
                    #pygame.Sound.play()
                    #pygame.mixer.Sound.play(eachNote.sound)
                    #Data.active_notes.append(eachNote)
                    
                    #the_sound = eachNote.sound

                    #pygame.mixer.find_channel(True)
                
                    #pygame.mixer.Sound.play(the_sound)

                    Data.note_count -= 1

                except Exception as info:
                    print(info)
                    #db.Data.debug_log = info
                    crash_me_A = pygame.quit()
                    crash_me_B = sys.exit()
                    crash_me_A
                    crash_me_B'''

        advance()

    else:
        t.Data.current_timer = t.Data.fast
        reset_meter()  # is this correct?
        g.Data.current_gate = 'post_production'
        d_i.Data.current_screen = 'post_production_screen'

        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?
