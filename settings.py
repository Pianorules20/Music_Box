#settings.py
import tones as t

master_volume = 0.5

class Data(): 
    
    tonesFor1stVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor1stVoice = 0.5
    tonesFor2ndVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor2ndVoice = 0.5
    tonesFor3rdVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor3rdVoice = 0.5
    tonesFor4thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5] 
    volumeFor4thVoice = 0.5 
    tonesFor5thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor5thVoice = 0.5
    tonesFor5thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor5thVoice = 0.5
    tonesFor6thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor6thVoice = 0.5
    tonesFor7thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor7thVoice = 0.5
    tonesFor8thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor8thVoice = 0.5
    tonesFor9thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor9thVoice = 0.5
    tonesFor10thVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor10thVoice = 0.5

    tonesInstruments = [tonesFor1stVoice, tonesFor2ndVoice, tonesFor3rdVoice, tonesFor4thVoice, tonesFor5thVoice, \
                        tonesFor6thVoice, tonesFor7thVoice, tonesFor8thVoice, tonesFor9thVoice, tonesFor10thVoice]

    metronome = 72
    metronomeModifier = 1
    dottedWholeNote = metronome*48
    wholeNote = metronome*32
    dottedHalfNote = metronome*24
    halfNote = metronome*16
    dottedQuarterNote = metronome*12
    quarterNote = metronome*8
    dottedEighthNote = metronome*6
    eighthNote = metronome*4
    dottedSixteenthNote = metronome*3
    sixteenthNote = metronome*2
    thirtySecondNote = metronome
    beats = [dottedWholeNote, wholeNote, dottedHalfNote, halfNote, dottedQuarterNote, quarterNote, \
            dottedEighthNote, eighthNote, dottedSixteenthNote, sixteenthNote, thirtySecondNote]
    dottedWholeRest = metronome*48
    wholeRest = metronome*32
    dottedHalfRest = metronome*24
    halfRest = metronome*16
    dottedQuarterRest = metronome*12
    quarterRest = metronome*8
    dottedEighthRest = metronome*6
    eighthRest = metronome*4
    dottedSixteenthRest = metronome*3
    sixteenthRest = metronome*2
    thirtySecondRest = metronome

    voice1 = 'Piano'
    voice2 = 'Piano'
    voice3 = 'Piano'
    voice4 = 'Piano'
    voice5 = 'Piano'
    voice6 = 'Piano'
    voice7 = 'Piano'
    voice8 = 'Piano'
    voice9 = 'Piano'
    voice10 = 'Piano'
    voices = [voice1, voice2, voice3, voice4, voice5, voice6, voice7, voice8, voice9, voice10]
    
    polyOrderList = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
    
    tonic = 'Random'
    
    motiveOption = 'Random'
    motiveOptions = ['Random', 'Custom']
    motiveRhythmOption = 'Random'
    motiveRhythmOptions = ['Random', 'Custom']
    
    motiveTones  = [t.Piano.B5, t.Piano.C5, t.Piano.A5, t.Piano.D5, t.Piano.B5, t.Piano.C5, \
                    t.Piano.G4, t.Piano.D5, t.Piano.C5] 
    motiveRhythm = [eighthNote, eighthNote, quarterNote, quarterNote, quarterNote, quarterNote, eighthNote, \
                    eighthNote, halfNote]
    
    harmony1 = tonesFor1stVoice[2]
    harmony2 = tonesFor1stVoice[3]
    harmony3 = tonesFor1stVoice[4]
    harmony4 = tonesFor1stVoice[6]
    harmonies = 'Standard'
    harmonyOptions = ['Standard', 'Custom']

    cadenza = 'Standard'        
    cadenzaOptions = ['Standard', 'Custom']
    cadenzaOver = tonesFor1stVoice[1]
    cadenzaUnder = tonesFor1stVoice[7]
    cadenzaDurationOver = beats[2]
    cadenzaDurationUnder = beats[3]
    
    #for best debugging change structure to another option in 'structureOptions'
    structure  = 'Random Short Form'
    structureOptions = ['Random Short Form', 'Long Form New', 'User Constructed']
    
    changeSettingsBetweenSections = False
    notesRemainingOption = 'Random'
    notesRemaining = int(80)

    rigidTempo = False #use me in future to differentiate between 'loose' studying music and 'firm' driven music

    #volume = 0.3
    master_volume = 10

    repeat_composition = False
    new_composition = True
    #pygame.mixer.Sound.set_volume(t.Piano.A1, 0.3)
    
    '''def addSounds():
        newSounds = []
        for each in upload.NewSounds.added:
            new = Tone(name = upload.NewSounds.added, sound = pygame.mixer.Sound(upload.NewSounds.sonic))
            newSounds.append(new)
        Preferences.newSounds = newSounds'''