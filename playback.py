#play.py 
import mySong, generate_notes_interface, playbackMeter, settings, pygame, gatekeeper, timer as t
from pygame.locals import *

#timer = pygame.time.get_ticks()
#print(f'metronome: {settings.Preferences.metronome}')

class Player():

    recording = []

    def play():

        t.Timer.current = t.Timer.fast
        print('playing!')

        #Player.clock.tick(round(settings.Preferences.metronome/settings.Preferences.metronomeModifier))
                
        '''for eachNote in eachSection:

            xPos = create_note.Note.returnXPos(eachNote)
            if xPos == playbackMeter.Meter.meter:  # this is the most important line hereS
                name = create_note.Note.returnLetterName(eachNote)
                octave = create_note.Note.returnOctave(eachNote)
                yPos = create_note.Note.returnYPos(eachNote) 
                sound = create_note.Note.returnSound(eachNote)           
                try:
                    create_note.Note.play(sound)
                    print(f'playing note data xPos {xPos} {name}{octave} yPos{yPos}')
                    section -= 1
                    print(f'keep going! {section}')
                except Exception as e:
                    print('Exception during play.Player.play')
                    print(e)
                            
                        else:
                            pass
                    playbackMeter.Meter.advance()
            else:
                playbackMeter.Meter.reset()'''
        #mySongs.Recordings.play = False
        
        #TROUBLESHOOT NOTES I AM ONLY GETTING ONE NOTE AT A TIME WHY IS THAT?