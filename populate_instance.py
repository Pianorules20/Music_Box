#populate_settings.py
import settings as s, current_section as c_s, random, tones as t, user_sounds, pygame, gni, structure as st

class Data():

    randInteger:int
    randVoice:s.Data
    randBeat:s.Data
    randBeat2:s.Data
    motive:list = []
    ranger:int

def createRemainingNotes():
    print('in populate_instance createRemainingNotes()')
    Data.randInteger = random.randint(40, 120)
    c_s.Data.notesRemaining = Data.randInteger
    st.Data.save_place = c_s.Data.notesRemaining
    print(f'in populate instance notes remaining -> c_s {Data.randInteger} ')
    #db.Data.debug_log.append(info)                           
        
def create_tonic():
    print('in populate_instance create_tonic()')
    print(' ')
    Data.randVoice = random.choice(s.Data.tonesFor1stVoice)
    c_s.Data.tonic = Data.randVoice
    Name = t.Tone.returnLetterName(Data.randVoice)
    Octave = t.Tone.returnOctave(Data.randVoice)
    info = f'tonic is {Name}{Octave}'
    print(info)
    #db.Data.debug_log.append(info)


def createMotiveTones():
    print('in populate_intance createMotiveTones()')
    print(' ')
    c_s.Data.motive = []
    Data.randInteger = random.randint(2, 13)       
    c_s.Data.motiveInteger = Data.randInteger
    for eachIndex in range(c_s.Data.motiveInteger):
        Data.randVoice = random.choice(s.Data.tonesFor1stVoice)
        c_s.Data.motive.append(Data.randVoice)
    #Data.motive = []
    for eachObj in c_s.Data.motive:
        Name = t.Tone.returnLetterName(eachObj)
        Data.motive.append(Name)
        Octave = str(t.Tone.returnOctave(eachObj))
        Data.motive.append(Octave)
        Data.motive.append(' ')
    info = 'newly created motive'
    print(info)
    info = print(*Data.motive, sep = '')
    info = info
    print('')

def createMotiveRhythm():
    print('in populate_instane createMotiveRhythm()')
    print(' ')
    c_s.Data.motiveRhythm = []
    Data.ranger = len(c_s.Data.motive)
    for eachInteger in range(Data.ranger):
        Data.randBeat = random.choice(c_s.Data.beats)    
        c_s.Data.motiveRhythm.append(Data.randBeat)
    info = f'in populate_instance, motive rhythm = {c_s.Data.motiveRhythm}'
    print(info)
    print(' ')

def createHarmonies():
    print('in populate_instance createHarmonies()')
    try:
        c_s.Data.harmony1 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed+2]  #adding integers
    except:
        c_s.Data.harmony1 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed-5]

    try:
        c_s.Data.harmony2 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed+3]
    except:
        c_s.Data.harmony2 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed-4]
    try:
        c_s.Data.harmony3 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed+4]
    except:
        c_s.Data.harmony3 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed-3]
    try:
        c_s.Data.harmony4 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed+5]
    except:
        c_s.Data.harmony4 = c_s.Data.tonesFor1stVoice[c_s.Data.indexed-2]
    print(f'harmonies: {c_s.Data.harmony1}, {c_s.Data.harmony2} {c_s.Data.harmony3}, {c_s.Data.harmony4}')
    
def createCadenza():
    print('in populate_instance createCadenza()')
    try:
        c_s.Data.cadenzaUnder = c_s.Data.tonesFor1stVoice[c_s.Data.indexed-1]
    except: 
        c_s.Data.cadenzaUnder = c_s.Data.tonesFor1stVoice[c_s.Data.indexed]
    try:
        c_s.Data.cadenzaOver = c_s.Data.tonesFor1stVoice[c_s.Data.indexed+1]
    except: 
        c_s.Data.cadenzaOver = c_s.Data.tonesFor1stVoice[c_s.Data.indexed]
    Name1 = t.Tone.returnLetterName(c_s.Data.cadenzaUnder)
    Octave1 = t.Tone.returnOctave(c_s.Data.cadenzaUnder)
    Name2 = t.Tone.returnLetterName(c_s.Data.cadenzaOver)
    Octave2 = t.Tone.returnOctave(c_s.Data.cadenzaOver)
    info = f'cadenza Under: {Name1}{Octave1}    cadenza Over: {Name2}{Octave2}'
    print(info)

    Data.randBeat = random.choice(c_s.Data.beats)
    Data.randBeat2 = random.choice(c_s.Data.beats)
    c_s.Data.cadenzaDurationUnder = Data.randBeat
    c_s.Data.cadenzaDurationOver = Data.randBeat2
    print(f'cadenza durations: {c_s.Data.cadenzaDurationOver}, {c_s.Data.cadenzaDurationUnder}')

    
def set_master_volume(userInteger):
    for eachObject in user_sounds.mySounds:
        Sound = gni.Note.returnSound(eachObject)
        pygame.mixer.Sound.set_volume(Sound, userInteger/10)
    for eachObject in t.Piano.tones:
        pygame.mixer.Sound.set_volume(eachObject.sound, userInteger/10)

def initialize():

    c_s.Data.tonesFor1stVoice = s.Data.tonesFor1stVoice
    print(f'in populate_instance initialize() tonesFor1stVoice {s.Data.tonesFor1stVoice}')
    
    if s.Data.tonic == 'Random':
        create_tonic()
    else:       
        c_s.Data.tonic = s.Data.tonic
        print(f'in populate_instance  init... old tonic = {s.Data.tonic}')
    
    indexTonic = s.Data.tonesFor1stVoice.index(c_s.Data.tonic)
    c_s.Data.indexed = indexTonic
    print(f'in populate_instance init... instance tonic indexed {c_s.Data.indexed}')
    
    if s.Data.motiveOption == 'Random':
        createMotiveTones()
    else:
        c_s.Data.motive = s.Data.motiveTones
        c_s.Data.motiveInteger = len(c_s.Data.motive)
        info = f'in populate_instance init...old motive. length: {len(c_s.Data.motive)} motive: {s.Data.motiveTones}'
        print(info)
    #db.Data.debug_log.append(info)

    c_s.Data.beats = s.Data.beats
    print(f'in populate_instance init... instantiating beats {s.Data.beats}')
    c_s.Data.metronome = s.Data.metronome
    print(f'in populate_instance init... instantiating metronome {s.Data.metronome}')

    if s.Data.motiveRhythmOption == 'Random':
        createMotiveRhythm()
    else:
        c_s.Data.motiveRhythm = s.Data.motiveRhythm
        info = f'in populate_instance init... old motive rhythm {s.Data.motiveRhythm} - length: {len(c_s.Data.motiveRhythm)}'
        print(info)
        #db.Data.debug_log = info
    print(' ')

    if s.Data.cadenza == 'Standard':
        createCadenza()
    else:
        c_s.Data.cadenzaOver = s.Data.cadenzaOver
        c_s.Data.cadenzaUnder = s.Data.cadenzaUnder
        c_s.Data.cadenzaDurationOver = s.Data.cadenzaDurationOver
        c_s.Data.cadenzaDurationUnder = s.Data.cadenzaDurationUnder
        print(f'in populate_instance init... using old candenzas {s.Data.cadenzaOver}{s.Data.cadenzaDurationOver}, {s.Data.cadenzaUnder}{s.Data.cadenzaDurationUnder}')
    print('')    
    
    if s.Data.notesRemainingOption == 'Random':
        createRemainingNotes()
    else:
        c_s.Data.notesRemaining = s.Data.notesRemaining
        info = f'in populate_instance init...using old notes remaining {c_s.Data.notesRemaining}'
        print(info)
        #db.Data.debug_log.append(info)
    print('')

    if s.Data.harmonies == 'Standard':
        createHarmonies()
    else:
        c_s.Data.harmony1 = s.Data.harmony1
        c_s.Data.harmony2 = s.Data.harmony2
        c_s.Data.harmony3 = s.Data.harmony3
        c_s.Data.harmony4 = s.Data.harmony4
        info = f'in populate_instance init...using old harmonies {s.Data.harmony1}, {s.Data.harmony2}, {s.Data.harmony3}, {s.Data.harmony4}'
        print(info)
        #db.Data.debug_log.append(info)
    print('')
    set_master_volume(s.Data.master_volume)
