'''def generate(x):
        clock = pygame.time.Clock()
        speed = clock.tick(settings.Preferences.metronome/20)
        timer = pygame.time.get_ticks()
        #print(f'metronome: {settings.Preferences.metronome}')
        if Note.process == None:
            Note.randomizer = random.random()
        elif Note.process == 'early':
            Note.randomizer = 0.3
        elif Note.process == 'early middle':
            Note.randomizer = 0.7
        elif Note.process == 'middle':
            Note.randomizer = 0.8
        elif Note.process == 'late':
            Note.randomizer = 0.95
        elif Note.process == 'last':
            randomizer = 1   
        polyOrder = settings.Preferences.instruments[0]
           
            #early randomizer is based on the generated motive
        if Note.randomizer  <= 0.3:
            print(' \n in early randomizer - the motive')
            for eachIndex in range(len(Note.motive)):
                settings.Preferences.currentNote = Note.motive[eachIndex]
                try:    
                    Note.currentDuration = settings.Preferences.motiveRhythm[eachIndex]
                    Name = settings.Tone.returnLetterName(settings.Preferences.currentNote)
                    Octave = settings.Tone.returnOctave(settings.Preferences.currentNote)
                    settings.Tone.current = settings.Tone.returnSound(settings.Preferences.currentNote)
                except Exception as f:
                    print('error in Step3 early randomizer with settings...motiveRhythm[eachIndex]')
                    Note.currentDuration = settings.Preferences.pulse
                    Name = settings.Tone.returnLetterName(settings.Preferences.currentNote)
                    Octave = settings.Tone.returnOctave(settings.Preferences.currentNote)
                    settings.Tone.current = settings.Tone.returnSound(settings.Preferences.currentNote) 
                try:      
                    settings.Tone.play(settings.Tone.current)
                    clock.tick(Note.currentDuration/(2*settings.Preferences.metronome))
                except Exception as e:
                        print('error in Step3 early randomizer')
                        
                        print(e) 
                        print(settings.Preferences.currentNote, settings.Tone.returnLetterName(settings.Preferences.currentNote), \
                                  settings.Tone.returnOctave(settings.Preferences.currentNote))
                # print(f'{Name}{Octave}')
                create.Creation.createNote(pitch = settings.Preferences.currentNote, duration = Note.currentDuration,\
                                               instrument =  settings.Preferences.instrument1,   
                                             polyOrder =  polyOrder,
                                                image = 'images/eighthNote.png')  
                Note.remaining -=1
                    #print(f'in Step3...early randomizer Notes remaining this section: {Note.remaining}')
            #early middle randomizer is based on the generated harmonies
        elif Note.randomizer <= 0.7: #None type errors found here
            print(f' \n in early middle randomizer Note.harmonies')
            randHarmony = random.randint(0,3)
            randbeat = random.choice(Note.beats)
            settings.Preferences.currentNote = random.choice(Note.harmonies)
            Note.currentDuration = randbeat
            Name = settings.Tone.returnLetterName(settings.Preferences.currentNote)
            Octave = settings.Tone.returnOctave(settings.Preferences.currentNote)
            
            sound = settings.Tone.returnSound(settings.Preferences.currentNote)
            try:
                settings.Tone.play(sound)
                clock.tick(Note.currentDuration/20)
            except Exception as e:
                    print('error in Step3 early middle randomizer')
                    print(e)
            print(f'{Name}{Octave}')
            create.Creation.createNote(pitch = settings.Preferences.currentNote, duration = Note.currentDuration, \
                                            instrument = settings.Preferences.instrument1,   
                                             polyOrder =  polyOrder,
                                                image = 'images/eighthNote.png')             
            Note.remaining -=1
            # middle randomizer is based on the cadenza notes in music theory they are 2 and 7
        elif Note.randomizer <=0.8:
            print(' \n in middle randomizer - cadenzas notes')
            overUnder = random.random()
            if overUnder <= 0.5:
                settings.Preferences.currentNote = Note.cadenzaUnder
                Note.currentDuration = Note.cadenzaDurationUnder
            elif overUnder <=1:
                settings.Preferences.currentNote = Note.cadenzaOver
                Note.currentDuration = Note.cadenzaDurationOver
            sound = settings.Tone.returnSound(settings.Preferences.currentNote)
            try:
                settings.Tone.play(sound)
                clock.tick(Note.currentDuration/20)     
            except Exception as e: 
                print('error in middle randomizer')
                print(e)
            create.Creation.createNote(pitch = settings.Preferences.currentNote, duration = Note.currentDuration,\
                                            instrument =  settings.Preferences.instrument1,   
                                            polyOrder =  polyOrder,
                                            image = 'images/eighthNote.png') 
            Note.remaining -=1
            #the late randomizer is based on a random tone and random duration
        elif Note.randomizer <=0.95:
            print(' \n in late randomizer - random notes')
            rando = random.choice(Note.tonesFor1stInstrument)
            settings.Preferences.currentNote = rando
            randoRhythm = random.choice(Note.beats)
            Note.currentDuration = randoRhythm
            sound = settings.Tone.returnSound(settings.Preferences.currentNote)
            try:
                settings.Tone.play(sound)
                clock.tick(Note.currentDuration/20)
            except Exception as e:
                print('error in late randomizer')
                print(e)
            create.Creation.createNote(pitch = settings.Preferences.currentNote, duration = Note.currentDuration,\
                                            instrument =  settings.Preferences.instrument1,   
                                            polyOrder =  polyOrder,
                                            image = 'images/eighthNote.png') 
            Note.remaining -1
            # the last randomizer is the tonic itself       
        else:
            print(' \n in last randomizer - the tonic')
            settings.Preferences.currentNote = Note.tonic
            Note.currentDuration = random.choice(Note.beats)              
            sound = settings.Tone.returnSound(settings.Preferences.currentNote)
            try:
                settings.Tone.play(sound)
                clock.tick(Note.currentDuration/20)
            except Exception as e:
                print('error in last randomizer') 
                print(e)
            create.Creation.createNote(pitch = settings.Preferences.currentNote, duration = Note.currentDuration,\
                                            instrument =  settings.Preferences.instrument1,   
                                            polyOrder =  polyOrder,
                                            image = 'images/eighthNote.png')
            Note.remaining -=1 
        print(f'notes remaining this section: {Note.remaining}')
        Note.process = None  
        if Note.remaining > 0:
            Note.pathSet = True
        else: 
            Note.pathSet = False
            mySongs.Recordings.appendSection(x)'''