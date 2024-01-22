#introSound.py
import pygame, tones
    
    #modify the script below to change volume of the intro harp
for eachSound in tones.Harp.introMusic:
    Sound = tones.Tone.returnSound(eachSound)
    pygame.mixer.Sound.set_volume(Sound, 0.3) 

for eachSound in tones.Piano.tones:
    Sound = tones.Tone.returnSound(eachSound)
    pygame.mixer.Sound.set_volume(Sound, 2)

class Intro():
    clock = pygame.time.Clock()
    
def play():
    '''try:
        
        test = pygame.mixer.Sound.play(settings.Preferences.A3.sound)
        print('playing test sound')
        
    except:
        print('failed test sound')'''
    try :
        length = len(tones.Harp.introMusic)
        for eachInteger in range(length):
            note = tones.Harp.introMusic[eachInteger]   
            pygame.mixer.find_channel(True)
            sound = tones.Tone.returnSound(note)
            pygame.mixer.Sound.play(sound)
            Intro.clock.tick(10)
            #pygame.time.wait(170)
        print('playing intro')
    except Exception as e:
        print('failed to play introMusic.Intro.play')
        print(e)

    finally:
        letterName = tones.Tone.returnLetterName(note)
        octave = tones.Tone.returnOctave(note)
        print(f'Note spacial data xPos  {letterName}{octave}')