#generate_notes.py contains Generator (randomizer)

import random, settings as s, current_section as c_s, gni, my_song as m_s, tones as t

class Data():
    
    notes_generated:int = 0 #generate() contains the randomizer. it connects to step3 the note object creator
    randRest:s.Data
    currentNote: s.Data
    currentDuration: s.Data
    randomizer:float
    music:gni.Note
    

def select_image(current_duration):

    match current_duration:

        case s.Data.dottedWholeNote:
            imageIn = 'images/dottedWholeNoteCorrect.png'
        
        case s.Data.wholeNote:
            imageIn = 'images/wholeNoteCorrect.png'

        case s.Data.dottedHalfNote:
            imageIn = 'images/dottedHalfNoteCorrect.png'

        case s.Data.halfNote:
            imageIn = 'images/halfNoteCorrect.png'

        case s.Data.dottedQuarterNote:
            imageIn = 'images/dottedQuarterNoteCorrect.png'

        case s.Data.quarterNote:
            imageIn = 'images/quarterNoteCorrect.png'
        
        case s.Data.dottedEighthNote:
            imageIn = 'images/dottedEighthNoteCorrect.png'

        case s.Data.eighthNote:
            imageIn = 'images/eighthNoteCorrect.png'

        case s.Data.dottedSixteenthNote:
            imageIn = 'images/dottedSixteenthNoteCorrect.png'

        case s.Data.sixteenthNote:
            imageIn = 'images/sixteenthNoteCorrect.png'
        
        case s.Data.dottedWholeRest:
            imageIn = 'images/dottedWholeRestCorrect.png'
        
        case s.Data.wholeRest:
            imageIn = 'images/wholeRestCorrect.png'

        case s.Data.dottedHalfRest:
            imageIn = 'images/dottedHalfRestCorrect.png'

        case s.Data.halfRest:
            imageIn = 'images/halfRestCorrect.png'
        
        case s.Data.dottedQuarterRest:
            imageIn = 'images/dottedQuardterRestCorrect.png'

        case s.Data.quarterRest:
            imageIn = 'images/quarterRestCorrect.png'

        case s.Data.dottedEighthRest:
            imageIn = 'images/dottedEighthRestCorrect.png'
        
        case s.Data.eighthRest:
            imageIn = 'images/eighthRestCorrect.png'
        
        case s.Data.dottedSixteenthRest:
            imageIn = 'images/dottedSixteenthRestCorrect.png'

        case s.Data.sixteenthRest:
            imageIn = 'images/sixteenthRestCorrect.png'
        
        case s.Data.thirtySecondRest:
            imageIn = 'images/thirtySecondRestCorrect.png'
    
    return imageIn


def rectangle():
    pass

def generate(voice):


    Data.randomizer = random.random()

    match voice:
        
        case c_s.Data.tonesFor1stVoice:
    
            #currentNote = c_s.Data.tonic #initializes currentNote
            #currentDuration = settings.Data.quarterNote #initializes currentDuration
            
            #first randomizer: the rest
            if Data.randomizer <=0.15:
                info = f'\n _in_first_randomizer_-_rest_'
                print(info)
                Data.notes_generated = 0
                Data.randRest = random.choice(s.Data.beats)
                Data.currentDuration = Data.randRest

            #early randomizer is based on the generated motive'

            if Data.randomizer  <= 0.3:
                info = f'\n_in_early_randomizer_-_the_motive_'
                print(info)
                Data.notes_generated = len(c_s.Data.motive)    
                for eachIndex in range(len(c_s.Data.motive)):
                    Data.currentNote = c_s.Data.motive[eachIndex]
                    Data.currentDuration = c_s.Data.motiveRhythm[eachIndex]
                    Data.imageIn = select_image(Data.currentDuration)
                    Data.music = gni.Note(sound = gni.Note.returnSound(Data.currentNote), duration = Data.currentDuration,
                            polyOrder = s.Data.voice1, \
                            letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                            xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
                    c_s.Data.current_section.append(Data.music)
                    m_s.Data.meter += Data.currentDuration
                    info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
                    print(info)
                    #db.Data.debug_log.append(info)
                # print(f'{Name}{Octave}')
            #early middle randomizer is based on the generated harmonies
            elif Data.randomizer <= 0.7: #None type errors found here
                info = f' \n_in_early_middle_randomizer_c_s.harmonies_'
                print(info)
                #db.Data.debug_log.append(info)
                Data.notes_generated = 1
                Data.rando = random.choice(c_s.Data.harmonies)
                Data.currentNote = Data.rando
                Data.currentDuration = random.choice(c_s.Data.beats)
                Data.imageIn = select_image(Data.currentDuration)
                Data.music = gni.Note(sound = gni.Note.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice1, \
                    letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight, imageOut = Data.imageIn)
                c_s.Data.current_section.append(Data.music)
                m_s.Data.meter += Data.currentDuration
                info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
                print(info)
                #db.Data.debug_log.append(info)
            # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
            elif Data.randomizer <=0.8:
                info = f' \n_in_middle_randomizer_-_cadenzas_notes'
                print(info)
                #db.Data.debug_log.append(info)
                Data.overUnder = random.random()
                Data.notes_generated = 1
                if Data.overUnder <= 0.5:
                    Data.currentNote = c_s.Data.cadenzaUnder
                    Data.currentDuration = c_s.Data.cadenzaDurationUnder
                elif Data.overUnder <=1:
                    Data.currentNote = c_s.Data.cadenzaOver
                    Data.currentDuration = c_s.Data.cadenzaDurationOver
                Data.imageIn = select_image(Data.currentDuration)
                Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice1, \
                    letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
                c_s.Data.current_section.append(Data.music)
                m_s.Data.meter += Data.currentDuration
                info = f' in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
                print(info)
                #db.Data.debug_log.append(info)
            elif Data.randomizer <= 0.95:
                info = f' \n_in_late_randomizer_-_random_notes'
                print(info)
                #db.Data.debug_log.append(info)
                Data.notes_generated = 1
                Data.rando = random.choice(c_s.Data.tonesFor1stVoice)
                Data.currentNote = Data.rando
                Data.randoRhythm = random.choice(c_s.Data.beats)
                Data.currentDuration = Data.randoRhythm
                Data.imageIn = select_image(Data.currentDuration)
                Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice1, \
                    letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
                c_s.Data.current_section.append(Data.music)
                m_s.Data.meter += Data.currentDuration
                info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
                print(info)
                #db.Data.debug_log.append(info)
            # the last randomizer is the tonic itself       
            else:
                info = f' \n_in_last_randomizer_-_the_tonic'
                print(info)
                #db.Data.debug_log.append(info)    
                Data.notes_generated = 1 
                Data.currentNote = c_s.Data.tonic
                Data.randoRhythm = random.choice(c_s.Data.beats)   
                Data.currentDuration = Data.randoRhythm  
                Data.imageIn = select_image(Data.currentDuration)       
                Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice1, \
                    letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                    xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
                c_s.Data.current_section.append(Data.music)
                m_s.Data.meter += Data.currentDuration
                info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}'
                print(info)
                #db.Data.debug_log.append(info)
        
        case c_s.Data.tonesFor2ndVoice:
            
            info = f' \n_in_2nd_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor2ndVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice2, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f' in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

        case c_s.Data.tonesFor3rdVoice:

            info = f' \n_in_3rd_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor3rdVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice3, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

        case c_s.Data.tonesFor4thVoice:

            info = f' \n_in_4th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor4thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice4, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

        case c_s.Data.tonesFor5thVoice:

            info = f' \n_in_5th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor5thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice5, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)
        

        case c_s.Data.tonesFor6thVoice:

            info = f' \n_in_6th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor6thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice6, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)

        case c_s.Data.tonesFor7thVoice:

            info = f' \n_in_7th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor7thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice7, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)

        case c_s.Data.tonesFor8thVoice:

            info = f' \n_in_8th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor8thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice8, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)

        case c_s.Data.tonesFor9thVoice:

            info = f' \n_in_9th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor9thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice9, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)

        case c_s.Data.tonesFor10thVoice:

            info = f' \n_in_10th_voice'
            print(info)
            #db.Data.debug_log.append(info)
            Data.notes_generated = 1
            Data.rando = random.choice(c_s.Data.tonesFor10thVoice)
            Data.currentNote = Data.rando
            Data.randoRhythm = random.choice(c_s.Data.beats)
            Data.currentDuration = Data.randoRhythm
            Data.imageIn = select_image(Data.currentDuration)
            Data.music = gni.Note(sound = t.Tone.returnSound(Data.currentNote), duration = Data.currentDuration, polyOrder = s.Data.voice10, \
                letterName = t.Tone.returnLetterName(Data.currentNote), octave = t.Tone.returnOctave(Data.currentNote),\
                xPos = m_s.Data.meter, yPos = t.Tone.returnClefHeight(Data.currentNote), imageOut = Data.imageIn)
            c_s.Data.current_section.append(Data.music)
            m_s.Data.meter += Data.currentDuration
            info = f'in generate_notes generate():_xPos_{Data.music.letterName}{Data.music.octave}_yPos_{Data.music.yPos}_'
            print(info)
            #db.Data.debug_log.append(info)

    #Data.notes_generated = data  # !!!!
    print(f'in g_n, line 239, current_section = {c_s.Data.current_section}')
    #gatekeeper.Gate.passGate('generate_notes')
    #else:
    #    cs.transcribe_section()
