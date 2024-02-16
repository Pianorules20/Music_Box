#step2 contains Generator (randomizer)

import random, settings as sett, current_section as c_s, gni, debug as db, my_song as m_s, tones as t

class Data():
    
    notes_generated = int(1) #generate() contains the randomizer. it connects to step3 the note object creator

def select_image(current_duration):

    match current_duration:

        case sett.Data.dottedWholeNote:
            imageIn = 'images/dottedWholeNoteCorrect.png'
        
        case sett.Data.wholeNote:
            imageIn = 'images/wholeNoteCorrect.png'

        case sett.Data.dottedHalfNote:
            imageIn = 'images/dottedHalfNoteCorrect.png'

        case sett.Data.halfNote:
            imageIn = 'images/halfNoteCorrect.png'

        case sett.Data.dottedQuarterNote:
            imageIn = 'images/dottedQuarterNoteCorrect.png'

        case sett.Data.quarterNote:
            imageIn = 'images/quarterNoteCorrect.png'
        
        case sett.Data.dottedEighthNote:
            imageIn = 'images/dottedEighthNoteCorrect.png'

        case sett.Data.eighthNote:
            imageIn = 'images/eighthNoteCorrect.png'

        case sett.Data.dottedSixteenthNote:
            imageIn = 'images/dottedSixteenthNoteCorrect.png'

        case sett.Data.sixteenthNote:
            imageIn = 'images/sixteenthNoteCorrect.png'
    
    return imageIn


def rectangle():
    pass

def generate(voice):


    randomizer = random.random()

    match voice:
        
        case c_s.Data.tonesFor1stVoice:
    
            #currentNote = c_s.Data.tonic #initializes currentNote
            #currentDuration = settings.Data.quarterNote #initializes currentDuration
            
            #early randomizer is based on the generated motive'

            if randomizer  <= 0.3:
                info = f'\n_in_early_randomizer_-_the_motive_'
                print(info)
                #db.Data.debug_log.append(info)   
                data = len(c_s.Data.motive)    
                for eachIndex in range(len(c_s.Data.motive)):
                    currentNote = c_s.Data.motive[eachIndex]
                    currentDuration = c_s.Data.motiveRhythm[eachIndex]
                    imageIn = select_image(currentDuration)
                    music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice1, \
                        letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                        xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
                    c_s.Data.current_section.append(music)
                    m_s.Data.meter += currentDuration
                    info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
                    print(info)
                    #db.Data.debug_log.append(info)
                # print(f'{Name}{Octave}')
            #early middle randomizer is based on the generated harmonies
            elif randomizer <= 0.7: #None type errors found here
                info = f' \n_in_early_middle_randomizer_cs.harmonies_'
                print(info)
                #db.Data.debug_log.append(info)
                data = 1
                rando = random.choice(c_s.Data.harmonies)
                currentNote = rando
                currentDuration = random.choice(c_s.Data.beats)
                imageIn = select_image(currentDuration)
                music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice1, \
                    letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
                c_s.Data.current_section.append(music)
                m_s.Data.meter += currentDuration
                info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
                print(info)
                #db.Data.debug_log.append(info)
            # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
            elif randomizer <=0.8:
                info = f' \n_in_middle_randomizer_-_cadenzas_notes'
                print(info)
                #db.Data.debug_log.append(info)
                overUnder = random.random()
                data = 1
                if overUnder <= 0.5:
                    currentNote = c_s.Data.cadenzaUnder
                    currentDuration = c_s.Data.cadenzaDurationUnder
                elif overUnder <=1:
                    currentNote = c_s.Data.cadenzaOver
                    currentDuration = c_s.Data.cadenzaDurationOver
                imageIn = select_image(currentDuration)
                music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice1, \
                    letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
                c_s.Data.current_section.append(music)
                m_s.Data.meter += currentDuration
                info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
                print(info)
                #db.Data.debug_log.append(info)
            elif randomizer <= 0.95:
                info = f' \n_in_late_randomizer_-_random_notes'
                print(info)
                #db.Data.debug_log.append(info)
                data = 1
                rando = random.choice(c_s.Data.tonesFor1stVoice)
                currentNote = rando
                randoRhythm = random.choice(c_s.Data.beats)
                currentDuration = randoRhythm
                imageIn = select_image(currentDuration)
                music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice1, \
                    letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
                c_s.Data.current_section.append(music)
                m_s.Data.meter += currentDuration
                info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
                print(info)
                #db.Data.debug_log.append(info)
            # the last randomizer is the tonic itself       
            else:
                info = f' \n_in_last_randomizer_-_the_tonic'
                print(info)
                #db.Data.debug_log.append(info)    
                data = 1 
                currentNote = c_s.Data.tonic
                rando = random.choice(c_s.Data.beats)   
                currentDuration = rando    
                imageIn = select_image(currentDuration)       
                music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice1, \
                    letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
                c_s.Data.current_section.append(music)
                m_s.Data.meter += currentDuration
                info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}'
                print(info)
                #db.Data.debug_log.append(info)
        
        case c_s.Data.tonesFor2ndVoice:
            
            info = f' \n_in_2nd_voice'
            print(info)
            #db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor2ndVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = rando
            imageIn = select_image(currentDuration)
            music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice2, \
                letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
            c_s.Data.current_section.append(music)
            m_s.Data.meter += currentDuration
            info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

        case c_s.Data.tonesFor3rdVoice:

            info = f' \n_in_3rd_voice'
            print(info)
            #db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor3rdVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = random.choice(c_s.Data.beats)
            imageIn = select_image(currentDuration)
            music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice3, \
                letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
            c_s.Data.current_section.append(music)
            m_s.Data.meter += currentDuration
            info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

        case c_s.Data.tonesFor4thVoice:

            info = f' \n_in_4th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor4thVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = random.choice(c_s.Data.beats)
            imageIn = select_image(currentDuration)
            music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice4, \
                letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
            c_s.Data.current_section.append(music)
            m_s.Data.meter += currentDuration
            info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

        case c_s.Data.tonesFor5thVoice:

            info = f' \n_in_5th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor5thVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = random.choice(c_s.Data.beats)
            imageIn = select_image(currentDuration)
            music = gni.Note(sound = t.Tone.returnSound(currentNote), duration = currentDuration, polyOrder = sett.Data.voice5, \
                letterName = t.Tone.returnLetterName(currentNote), octave = t.Tone.returnOctave(currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = imageIn)
            c_s.Data.current_section.append(music)
            m_s.Data.meter += currentDuration
            info = f'_in_p_n:_xPos_{music.letterName}{music.octave}_yPos_{music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

    Data.notes_generated = data
    #gatekeeper.Gate.passGate('generate_notes')
    #else:
    #    cs.transcribe_section()