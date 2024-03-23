#populate_settings.py
import settings as s, current_section as c_s, random, tones as t, user_sounds, pygame, gni, debug as db, structure as st

def createRemainingNotes():
    
    rando = random.randint(40, 120)
    c_s.Data.notesRemaining = rando
    st.Data.save_place = c_s.Data.notesRemaining
        
    print(' ')
    rando = random.choice(s.Data.tonesFor1stVoice)
    c_s.Data.tonic = rando
    Name = t.Tone.returnLetterName(rando)
    Octave = t.Tone.returnOctave(rando)
    info = f'Tonic: {Name}{Octave}'
    print(info)    
    #db.Data.debug_log.append(info)                           
        
def create_tonic():
    print(' ')
    rando = random.choice(s.Data.tonesFor1stVoice)
    c_s.Data.tonic = rando
    info = f'tonic is {c_s.Data.tonic}'
    print(info)
    #db.Data.debug_log.append(info)


def createMotiveTones():
    print(' ')
    c_s.Data.motive = []
    rando = random.randint(2, 13)       
    c_s.Data.motiveInteger = rando
    for eachIndex in range(c_s.Data.motiveInteger):
        new = random.choice(s.Data.tonesFor1stVoice)
        c_s.Data.motive.append(new)
    motive = []
    for eachObj in c_s.Data.motive:
        Name = t.Tone.returnLetterName(eachObj)
        motive.append(Name)
        Octave = str(t.Tone.returnOctave(eachObj))
        motive.append(Octave)
        motive.append(' ')
    info = 'newly created motive'
    print(info)
    info = print(*motive, sep = '')
    info = info
    #db.Data.debug_log.append(info)
    print('')

def createMotiveRhythm():
    print(' ')
    c_s.Data.motiveRhythm = []
    for eachIndex in c_s.Data.motive:
        rando = random.choice(c_s.Data.beats)
        newDuration = rando     
        c_s.Data.motiveRhythm.append(newDuration)
    info = f'in populate_settings... motiveRhythm in current_section {c_s.Data.motiveRhythm}'
    print(info)
    #db.Data.debug_log.append(info)
    print(' ')

def createHarmonies():

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
    
def createCadenza():
        
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
    #db.Data.debug_log.append(info)
    cadenzaDuration = random.choice(c_s.Data.beats)
    index = c_s.Data.beats.index(cadenzaDuration)
    #print(f'assigned cadenza pulse in step2...maker {cadenzaDuration}')
    try:
        c_s.Data.cadenzaDurationUnder = c_s.Data.beats[index-1]
    except: c_s.Data.cadenzaDurationUnder = c_s.Data.beats[index]
    try:
        c_s.Data.cadenzaDurationOver = c_s.Data.beats[index+1]
    except: c_s.Data.cadenzaDurationOver = c_s.Data.beats[index]

    
def set_master_volume(userInteger):
    for eachObject in user_sounds.mySounds:
        Sound = gni.Note.returnSound(eachObject)
        pygame.mixer.Sound.set_volume(Sound, userInteger/10)

def initialize():
    
    #instance.voices = range(len(s.Data.VoicetonesFor1stVoices))

    c_s.Data.tonesFor1stVoice = s.Data.tonesFor1stVoice

    if s.Data.tonic == 'Random':
        create_tonic()
    else:       
        c_s.Data.tonic = s.Data.tonic
    
    indexTonic = s.Data.tonesFor1stVoice.index(c_s.Data.tonic)
    c_s.Data.indexed = indexTonic
    
    if s.Data.motiveOption == 'Random':
        createMotiveTones()
    else:
        c_s.Data.motive = s.Data.motiveTones
        c_s.Data.motiveInteger = len(c_s.Data.motive)
    info = f'in initializer: length of motive: {len(c_s.Data.motive)}'
    print(info)
    #db.Data.debug_log.append(info)

    c_s.Data.beats = s.Data.beats
    c_s.Data.metronome = s.Data.metronome

    if s.Data.motiveRhythmOption == 'Random':
        createMotiveRhythm()
    else:
        c_s.Data.motiveRhythm = s.Data.motiveRhythm
    info = f'in initializer: length of motive rhythm:{len(c_s.Data.motiveRhythm)}'
    print(info)
    db.Data.debug_log.append(info)
    print(' ')

    if s.Data.cadenza == 'Standard':
        createCadenza()
    else:
        c_s.Data.cadenzaOver = s.Data.cadenzaOver
        c_s.Data.cadenzaUnder = s.Data.cadenzaUnder
        c_s.Data.cadenzaDurationOver = s.Data.cadenzaDurationOver
        c_s.Data.cadenzaDurationUnder = s.Data.cadenzaDurationUnder
    print('')    
    
    if s.Data.notesRemainingOption == 'Random':
        createRemainingNotes()
    else:
        c_s.Data.notesRemaining = s.Data.notesRemaining
    info = f'in initializer: notes remaining {c_s.Data.notesRemaining}'
    print(info)
    #db.Data.debug_log.append(info)

    if s.Data.harmonies == 'Standard':
        createHarmonies()
    else:
        c_s.Data.harmony1 = s.Data.harmony1
        c_s.Data.harmony2 = s.Data.harmony2
        c_s.Data.harmony3 = s.Data.harmony3
        c_s.Data.harmony4 = s.Data.harmony4
    info = f'in initializer: refer to settings.Data.structure {s.Data.structure}'
    print(info)
    #db.Data.debug_log.append(info)

    if s.Data.notesRemainingOption == 'Random':
        createRemainingNotes()
    else:
        c_s.Data.notesRemaining = s.Data.notesRemaining 
        st.Data.save_place = c_s.Data.notesRemaining