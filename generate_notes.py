#step2 contains Generator (randomizer)

import random, settings, current_section as cs, gni, debug as db

class Generator():
    
    pass #generate() contains the randomizer. it connects to step3 the note object creator

def generate():
    currentNote = cs.Data.tonic #initializes currentNote
    currentDuration = settings.Data.quarterNote #initializes currentDuration

    polyOrder = settings.Data.instruments[0]
    
    #if cs.Data.notesRemaining > 0: #Note the use of the while loop to complete this section !!!!!
    db.Data.debug_log.append(f' in g_n notes remaining this i: {cs.Data.notesRemaining}')
    randomizer = random.random()
    
    #early randomizer is based on the generated motive
    if randomizer  <= 0.3:
        db.Data.debug_log.append(' \n in early randomizer - the motive')
        db.Data.debug_log.append(len(cs.Data.motive))
        db.Data.debug_log.append(len(cs.Data.motiveRhythm))        
        for eachIndex in range(len(cs.Data.motive)):
            currentNote = cs.Data.motive[eachIndex]
            currentDuration = cs.Data.motiveRhythm[eachIndex]
            gni.createNote(currentNote, currentDuration)
        # print(f'{Name}{Octave}')
    #early middle randomizer is based on the generated harmonies
    elif randomizer <= 0.7: #None type errors found here
        db.Data.debug_log.append(f' \n in early middle randomizer cs.harmonies')
        rando = random.choice(cs.Data.harmonies)
        currentNote = rando
        currentDuration = random.choice(cs.Data.beats)
        gni.createNote(currentNote, currentDuration)
    # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
    elif randomizer <=0.8:
        db.Data.debug_log.append(' \n in middle randomizer - cadenzas notes')
        overUnder = random.random()
        if overUnder <= 0.5:
            currentNote = cs.Data.cadenzaUnder
            currentDuration = cs.Data.cadenzaDurationUnder
        elif overUnder <=1:
            currentNote = cs.Data.cadenzaOver
            currentDuration = cs.Data.cadenzaDurationOver
        gni.createNote(currentNote, currentDuration)
    elif randomizer <= 0.95:
        db.Data.debug_log.append(' \n in late randomizer - random notes')
        rando = random.choice(cs.Data.tonesFor1stInstrument)
        currentNote = rando
        randoRhythm = random.choice(cs.Data.beats)
        currentDuration = randoRhythm
        gni.createNote(currentNote, currentDuration)
    # the last randomizer is the tonic itself       
    else:
        db.Data.debug_log.append(' \n in last randomizer - the tonic')     
        currentNote = cs.Data.tonic
        rando = random.choice(cs.Data.beats)   
        currentDuration = rando           
        gni.createNote(currentNote, currentDuration)
    #gatekeeper.Gate.passGate('generate_notes')
    #else:
    #    cs.transcribe_section()