#step2 contains Generator (randomizer)

import random, settings, mySong, instance, generate_notes_interface, playbackMeter

class Generator(): #generate() contains the randomizer. it connects to step3 the note object creator

    def generate():
        currentNote = instance.tonic #initializes currentNote
        currentDuration = settings.Preferences.quarterNote #initializes currentDuration

        polyOrder = settings.Preferences.instruments[0]
        
        while instance.notesRemaining > 0: #Note the use of the while loop to complete this section
            randomizer = random.random()
           
            #early randomizer is based on the generated motive
            if randomizer  <= 0.3:
                print(' \n in early randomizer - the motive')
                print(len(instance.motive))
                print(len(instance.motiveRhythm))        
                for eachIndex in range(len(instance.motive)):
                    currentNote = instance.motive[eachIndex]
                    currentDuration = instance.motiveRhythm[eachIndex]
                    generate_notes_interface.createNote(currentNote, currentDuration)
                # print(f'{Name}{Octave}')
            #early middle randomizer is based on the generated harmonies
            elif randomizer <= 0.7: #None type errors found here
                print(f' \n in early middle randomizer instance.harmonies')
                rando = random.choice(instance.harmonies)
                currentNote = rando
                currentDuration = random.choice(instance.beats)
                generate_notes_interface.createNote(currentNote, currentDuration)
            # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
            elif randomizer <=0.8:
                print(' \n in middle randomizer - cadenzas notes')
                overUnder = random.random()
                if overUnder <= 0.5:
                    currentNote = instance.cadenzaUnder
                    currentDuration = instance.cadenzaDurationUnder
                elif overUnder <=1:
                    currentNote = instance.cadenzaOver
                    currentDuration = instance.cadenzaDurationOver
                generate_notes_interface.createNote(currentNote, currentDuration)
            elif randomizer <= 0.95:
                print(' \n in late randomizer - random notes')
                rando = random.choice(instance.tonesFor1stInstrument)
                currentNote = rando
                randoRhythm = random.choice(instance.beats)
                currentDuration = randoRhythm
                generate_notes_interface.createNote(currentNote, currentDuration)
            # the last randomizer is the tonic itself       
            else:
                print(' \n in last randomizer - the tonic')     
                currentNote = instance.tonic
                rando = random.choice(instance.beats)   
                currentDuration = rando           
                generate_notes_interface.createNote(currentNote, currentDuration)
        print(f'notes remaining this section: {instance.notesRemaining}')
        mySong.Transcription.finished = True