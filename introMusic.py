#introSound.py
import pygame, sys, tones, timer as t, debug as db, display as d, fonts as f, screen_saver as ss
    
    #modify the script below to change volume of the intro harp

class Data():

    loading_A = "Playing Intro"
    loading_B = f.Data.large_script
    loading_C = loading_B.render(loading_A, True, ss.Data.text, ss.Data.rbg)
    loading_D = loading_C.get_rect()
    loading_D.center = (1000, 1000)

def play():
    
  
    d.Data.frame.blit(Data.loading_C, Data.loading_D)

    t.Data.current_timer = t.Data.slow

    #length = len(tones.Harp.introMusic)

    for eachSound in tones.Harp.introMusic:
        Sound = tones.Tone.returnSound(eachSound) 
        Data.letterName = tones.Tone.returnLetterName(eachSound)
        Data.octave = tones.Tone.returnOctave(eachSound)
        Data.info = f'{Data.letterName}{Data.octave}'  # note spacial data
        print(Data.info)
        db.Data.debug_log.append(Data.info)
        #Data.note = tones.Harp.introMusic[eachSound]  
    
        try :
             
            pygame.mixer.find_channel(True)
            #volume = pygame.mixer.Sound.set_volume(0.3)
            #volume = volume
            pygame.mixer.Sound.play(Sound)
            #Data.clock.tick(15)
            pygame.time.wait(125)
        
        except Exception as e:
            
            print('dev Exception in intoMusic.play')
            print(e)
            crash_me_A = pygame.quit()
            crash_me_B = sys.exit()


        finally:
            pass

        ''' Data.splash_A = "Press  'S'  to scroll through the log"
    Data.splash_B = f.Data.scripted
    Data.splash_C = Data.splash_B.render(Data.splash_A, True, ss.Data.text, ss.Data.rbg)
    Data.splash_D = Data.splash_C.get_rect()
    Data.splash_D.center = (1000, 50)
    d.Data.frame.blit(Data.splash_C, Data.splash_D)'''