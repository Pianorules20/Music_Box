#settings.py
import tones

master_volume = 0.3

class Data(): #Op stands for 'options'
    
    tonesFor1stInstrument = [tones.Piano.A4, tones.Piano.B4, tones.Piano.C4, tones.Piano.D4, tones.Piano.E4, \
                            tones.Piano.F4, tones.Piano.G4, tones.Piano.A5, tones.Piano.Bb5, tones.Piano.B5, \
                            tones.Piano.C5, tones.Piano.D5, tones.Piano.E5]
    tonesFor2ndInstrument = [tones.Piano.A2, tones.Piano.A3]
    tonesFor3rdInstrument = []
    tonesFor4thInstrument = []      
    tonesFor5thInstrument = []
    tonesInstruments = [tonesFor1stInstrument, tonesFor2ndInstrument, tonesFor3rdInstrument, \
                        tonesFor4thInstrument, tonesFor5thInstrument]
     
    metronome = 60
    metronomeModifier = 10
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
    
    motiveTones  = [tones.Piano.B5, tones.Piano.C5, tones.Piano.A5, tones.Piano.D5, tones.Piano.B5, tones.Piano.C5, \
                    tones.Piano.G4, tones.Piano.D5, tones.Piano.C5] 
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
    
    '''def addSounds():
        newSounds = []
        for each in upload.NewSounds.added:
            new = Tone(name = upload.NewSounds.added, sound = pygame.mixer.Sound(upload.NewSounds.sonic))
            newSounds.append(new)
        Preferences.newSounds = newSounds'''