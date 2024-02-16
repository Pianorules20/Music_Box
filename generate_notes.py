#step2 contains Generator (randomizer)

import random, settings as sett, current_section as c_s, gni, debug as db, my_song as m_s

class Data():
    
    notes_generated = int(1) #generate() contains the randomizer. it connects to step3 the note object creator

def select_image(current_duration):

    match current_duration:

        case sett.Data.dottedWholeNote:
            image = 'images/dottedWholeNoteCorrect.png'
        
        case sett.Data.wholeNote:
            image = 'images/wholeNoteCorrect.png'

        case sett.Data.dottedHalfNote:
            image = 'images/dottedHalfNoteCorrect.png'

        case sett.Data.halfNote:
            image = 'images/halfNoteCorrect.png'

        case sett.Data.dottedQuarterNote:
            image = 'images/dottedQuarterNoteCorrect.png'

        case sett.Data.quarterNote:
            image = 'images/quarterNoteCorrect.png'
        
        case sett.Data.dottedEighthNote:
            image = 'images/dottedEighthNoteCorrect.png'

        case sett.Data.eighthNote:
            image = 'images/eighthNoteCorrect.png'

        case sett.Data.dottedSixteenthNote:
            image = 'images/dottedSixteenthNoteCorrect.png'

        case sett.Data.sixteenthNote:
            image = 'images/sixteenthNoteCorrect.png'
    
    return image


def rectangle():
    pass

def generate(voice):


    randomizer = random.random()

    match voice:
        
        case c_s.Data.tonesFor1stVoice:
    
            #currentNote = c_s.Data.tonic #initializes currentNote
            #currentDuration = settings.Data.quarterNote #initializes currentDuration
            
            #early randomizer is based on the generated motive
            if randomizer  <= 0.3:
                info = f'\n_in_early_randomizer_-_the_motive_'
                print(info)
                db.Data.debug_log.append(info)   
                data = len(c_s.Data.motive)    
                for eachIndex in range(len(c_s.Data.motive)):
                    currentNote = c_s.Data.motive[eachIndex]
                    currentDuration = c_s.Data.motiveRhythm[eachIndex]
                    image = select_image(currentDuration)
                    gni.createNote(currentNote, currentDuration, image, polyOrderIn = sett.Data.voice1, )
                # print(f'{Name}{Octave}')
            #early middle randomizer is based on the generated harmonies
            elif randomizer <= 0.7: #None type errors found here
                info = f' \n_in_early_middle_randomizer_cs.harmonies_'
                print(info)
                db.Data.debug_log.append(info)
                data = 1
                rando = random.choice(c_s.Data.harmonies)
                currentNote = rando
                currentDuration = random.choice(c_s.Data.beats)
                image = select_image(currentDuration)
                gni.createNote(currentNote, currentDuration, image)
            # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
            elif randomizer <=0.8:
                info = f' \n_in_middle_randomizer_-_cadenzas_notes'
                print(info)
                db.Data.debug_log.append(info)
                overUnder = random.random()
                data = 1
                if overUnder <= 0.5:
                    currentNote = c_s.Data.cadenzaUnder
                    currentDuration = c_s.Data.cadenzaDurationUnder
                elif overUnder <=1:
                    currentNote = c_s.Data.cadenzaOver
                    currentDuration = c_s.Data.cadenzaDurationOver
                    image = select_image(currentDuration)
                gni.createNote(currentNote, currentDuration, image)
            elif randomizer <= 0.95:
                info = f' \n_in_late_randomizer_-_random_notes'
                print(info)
                db.Data.debug_log.append(info)
                data = 1
                rando = random.choice(c_s.Data.tonesFor1stVoice)
                currentNote = rando
                randoRhythm = random.choice(c_s.Data.beats)
                currentDuration = randoRhythm
                image = select_image(currentDuration)
                gni.createNote(currentNote, currentDuration, image)
            # the last randomizer is the tonic itself       
            else:
                info = f' \n_in_last_randomizer_-_the_tonic'
                print(info)
                db.Data.debug_log.append(info)    
                data = 1 
                currentNote = c_s.Data.tonic
                rando = random.choice(c_s.Data.beats)   
                currentDuration = rando    
                image = select_image(currentDuration)       
                gni.createNote(currentNote, currentDuration, image)
        
        case c_s.Data.tonesFor2ndVoice:
            
            info = f' \n_in_2nd_voice'
            print(info)
            db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor2ndVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = rando
            image = select_image(currentDuration)
            gni.createNote(currentNote, currentDuration, image)

        case c_s.Data.tonesFor3rdVoice:

            info = f' \n_in_3rd_voice'
            print(info)
            db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor3rdVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = random.choice(c_s.Data.beats)
            image = select_image(currentDuration)
            gni.createNote(currentNote, currentDuration, image)

        case c_s.Data.tonesFor4thVoice:

            info = f' \n_in_4th_voice'
            print(info)
            db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor4thVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = random.choice(c_s.Data.beats)
            image = select_image(currentDuration)
            gni.createNote(currentNote, currentDuration, image)

        case c_s.Data.tonesFor5thVoice:

            info = f' \n_in_5th_voice'
            print(info)
            db.Data.debug_log.append(info)
            data = 1
            rando = random.choice(c_s.Data.tonesFor5thVoice)
            currentNote = rando
            rando = random.choice(c_s.Data.beats)
            currentDuration = random.choice(c_s.Data.beats)
            image = select_image(currentDuration)
            gni.createNote(currentNote, currentDuration, image)

    Data.notes_generated = data
    #gatekeeper.Gate.passGate('generate_notes')
    #else:
    #    cs.transcribe_section()