#settings.py
import pygame, tones as t

master_volume = 0.3

class Data(): 
    
    tonesFor1stInstrument = [t.Piano.A4, t.Piano.B4, t.Piano.C4, t.Piano.D4, t.Piano.E4, \
                            t.Piano.F4, t.Piano.G4, t.Piano.A5, t.Piano.Bb5, t.Piano.B5, \
                            t.Piano.C5, t.Piano.D5, t.Piano.E5]
    volumeFor1stInstrument = 0.3
    tonesFor2ndInstrument = [t.Piano.A2, t.Piano.A3]
    volumeFor2ndInstrument = 0.3
    tonesFor3rdInstrument = []
    volumeFor3rdInstrument = 0.3
    tonesFor4thInstrument = []  
    volumeFor4thInstrument = 0.3 
    tonesFor5thInstrument = []
    volumeFor5thInstrument = 0.3
    tonesInstruments = [tonesFor1stInstrument, tonesFor2ndInstrument, tonesFor3rdInstrument, \
                        tonesFor4thInstrument, tonesFor5thInstrument]
     
    metronome = 60
    metronomeModifier = 3
    wholeNote = metronome*16
    halfNote = metronome*8
    quarterNote = metronome*4
    eighthNote = metronome*2
    sixteenthNote = metronome
    beats = [wholeNote, halfNote, quarterNote, eighthNote, sixteenthNote]

    instrument1 = 'Piano'
    instrument2 = 'Piano'
    instrument3 = 'Piano'
    instrument4 = 'Piano'
    instrument5 = 'Piano'
    instruments = [instrument1, instrument2, instrument3, instrument4, instrument5]
    
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
    
    harmony1 = tonesFor1stInstrument[2]
    harmony2 = tonesFor1stInstrument[3]
    harmony3 = tonesFor1stInstrument[4]
    harmony4 = tonesFor1stInstrument[6]
    harmonies = 'Standard'
    harmonyOptions = ['Standard', 'Custom']

    cadenza = 'Standard'        
    cadenzaOptions = ['Standard', 'Custom']
    cadenzaOver = tonesFor1stInstrument[1]
    cadenzaUnder = tonesFor1stInstrument[7]
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
    #pygame.mixer.Sound.set_volume(t.Piano.A1, 0.3)
    
    '''def addSounds():
        newSounds = []
        for each in upload.NewSounds.added:
            new = Tone(name = upload.NewSounds.added, sound = pygame.mixer.Sound(upload.NewSounds.sonic))
            newSounds.append(new)
        Preferences.newSounds = newSounds'''