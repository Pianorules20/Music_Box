#step2 contains Generator (randomizer)

import random, settings, current_section as cs, gni, debug as db

class Data():
    
    notes_generated = int(1) #generate() contains the randomizer. it connects to step3 the note object creator

def generate():
    
    currentNote = cs.Data.tonic #initializes currentNote
    currentDuration = settings.Data.quarterNote #initializes currentDuration

    polyOrder = settings.Data.instruments[0]
    
    #if cs.Data.notesRemaining > 0: #Note the use of the while loop to complete this section !!!!!
    #db.Data.debug_log.append(f'_in_generate_notes notes remaining this i: {cs.Data.notesRemaining}')
    randomizer = random.random()
    
    #early randomizer is based on the generated motive
    if randomizer  <= 0.3:
        info = f'\n_in_early_randomizer_-_the_motive_'
        print(info)
        db.Data.debug_log.append(info)   
        data = len(cs.Data.motive)    
        for eachIndex in range(len(cs.Data.motive)):
            currentNote = cs.Data.motive[eachIndex]
            currentDuration = cs.Data.motiveRhythm[eachIndex]
            gni.createNote(currentNote, currentDuration)
        # print(f'{Name}{Octave}')
    #early middle randomizer is based on the generated harmonies
    elif randomizer <= 0.7: #None type errors found here
        info = f' \n_in_early_middle_randomizer_cs.harmonies_'
        print(info)
        db.Data.debug_log.append(info)
        data = 1
        rando = random.choice(cs.Data.harmonies)
        currentNote = rando
        currentDuration = random.choice(cs.Data.beats)
        gni.createNote(currentNote, currentDuration)
    # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
    elif randomizer <=0.8:
        info = f' \n_in_middle_randomizer_-_cadenzas_notes'
        print(info)
        db.Data.debug_log.append(info)
        overUnder = random.random()
        data = 1
        if overUnder <= 0.5:
            currentNote = cs.Data.cadenzaUnder
            currentDuration = cs.Data.cadenzaDurationUnder
        elif overUnder <=1:
            currentNote = cs.Data.cadenzaOver
            currentDuration = cs.Data.cadenzaDurationOver
        gni.createNote(currentNote, currentDuration)
    elif randomizer <= 0.95:
        info = f' \n_in_late_randomizer_-_random_notes'
        print(info)
        db.Data.debug_log.append(info)
        data = 1
        rando = random.choice(cs.Data.tonesFor1stInstrument)
        currentNote = rando
        randoRhythm = random.choice(cs.Data.beats)
        currentDuration = randoRhythm
        gni.createNote(currentNote, currentDuration)
    # the last randomizer is the tonic itself       
    else:
        info = f' \n_in_last_randomizer_-_the_tonic'
        print(info)
        db.Data.debug_log.append(info)    
        data = 1 
        currentNote = cs.Data.tonic
        rando = random.choice(cs.Data.beats)   
        currentDuration = rando           
        gni.createNote(currentNote, currentDuration)

    Data.notes_generated = data
    #gatekeeper.Gate.passGate('generate_notes')
    #else:
    #    cs.transcribe_section()