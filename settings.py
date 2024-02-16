#settings.py
import tones as t

master_volume = 0.3

class Data(): 
    
    tonesFor1stVoice = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor1stVoice = 0.3
    tonesFor2ndVoice = [t.Piano.A2, t.Piano.A3, t.Piano.C3]
    volumeFor2ndVoice = 0.3
    tonesFor3rdVoice = [t.Piano.A1, t.Piano.E1, t.Piano.F1]
    volumeFor3rdVoice = 0.3
    tonesFor4thVoice = []  
    volumeFor4thVoice = 0.3 
    tonesFor5thVoice = []
    volumeFor5thVoice = 0.3
    tonesInstruments = [tonesFor1stVoice, tonesFor2ndVoice, tonesFor3rdVoice, \
                        tonesFor4thVoice, tonesFor5thVoice]
     
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
    beats = [dottedWholeNote, wholeNote, dottedHalfNote, halfNote, dottedQuarterNote, quarterNote, \
             dottedEighthNote, eighthNote, dottedSixteenthNote, sixteenthNote]

    voice1 = 'Piano'
    voice2 = 'Piano'
    voice3 = 'Piano'
    voice4 = 'Piano'
    voice5 = 'Piano'
    voices = [voice1, voice2, voice3, voice4, voice5]
    
    polyOrderList = ['1st', '2nd', '3rd', '4th', '5th']
    
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

    volume = 0.3

    repeat_composition = False
    #pygame.mixer.Sound.set_volume(t.Piano.A1, 0.3)
    
    '''def addSounds():
        newSounds = []
        for each in upload.NewSounds.added:
            new = Tone(name = upload.NewSounds.added, sound = pygame.mixer.Sound(upload.NewSounds.sonic))
            newSounds.append(new)
        Preferences.newSounds = newSounds'''