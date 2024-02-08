#pDataulates.py
import settings as s, current_section as cs, random, tones as t, user_sounds, pygame, gni, debug as db

def createRemainingNotes():
    
    rando = random.randint(40, 120)
    cs.Data.notesRemaining = rando
        
    print(' ')
    rando = random.choice(s.Data.tonesFor1stInstrument)
    cs.Data.tonic = rando
    Name = t.Tone.returnLetterName(rando)
    Octave = t.Tone.returnOctave(rando)
    info = f'Tonic: {Name}{Octave}'
    print(info)    
    db.Data.debug_log.append(info)                           
        
def create_tonic():
    print(' ')
    rando = random.choice(s.Data.tonesFor1stInstrument)
    cs.Data.tonic = rando
    info = f'tonic is {cs.Data.tonic}'
    print(info)
    db.Data.debug_log.append(info)


def createMotiveTones():
    print(' ')
    cs.Data.motive = []
    rando = random.randint(2, 13)       
    cs.Data.motiveInteger = rando
    for eachIndex in range(cs.Data.motiveInteger):
        new = random.choice(s.Data.tonesFor1stInstrument)
        cs.Data.motive.append(new)
    motive = []
    for eachObj in cs.Data.motive:
        Name = t.Tone.returnLetterName(eachObj)
        motive.append(Name)
        Octave = str(t.Tone.returnOctave(eachObj))
        motive.append(Octave)
        motive.append(' ')
    info = 'newly created motive'
    print(info)
    info = print(*motive, sep = '')
    info = info
    db.Data.debug_log.append(info)
    print('')

def createMotiveRhythm():
    print(' ')
    cs.Data.motiveRhythm = []
    for eachIndex in cs.Data.motive:
        rando = random.choice(cs.Data.beats)
        newDuration = rando     
        cs.Data.motiveRhythm.append(newDuration)
    info = f'in populate_settings... motiveRhythm in current_section {cs.Data.motiveRhythm}'
    print(info)
    db.Data.debug_log.append(info)
    print(' ')

def createHarmonies():

    try:
        cs.Data.harmony1 = cs.Data.tonesFor1stInstrument[cs.Data.indexed+2]  #adding integers
    except:
        cs.Data.harmony1 = cs.Data.tonesFor1stInstrument[cs.Data.indexed-5]

    try:
        cs.Data.harmony2 = cs.Data.tonesFor1stInstrument[cs.Data.indexed+3]
    except:
        cs.Data.harmony2 = cs.Data.tonesFor1stInstrument[cs.Data.indexed-4]
    try:
        cs.Data.harmony3 = cs.Data.tonesFor1stInstrument[cs.Data.indexed+4]
    except:
        cs.Data.harmony3 = cs.Data.tonesFor1stInstrument[cs.Data.indexed-3]
    try:
        cs.Data.harmony4 = cs.Data.tonesFor1stInstrument[cs.Data.indexed+5]
    except:
        cs.Data.harmony4 = cs.Data.tonesFor1stInstrument[cs.Data.indexed-2]
    
def createCadenza():
        
    try:
        cs.Data.cadenzaUnder = cs.Data.tonesFor1stInstrument[cs.Data.indexed-1]
    except: 
        cs.Data.cadenzaUnder = cs.Data.tonesFor1stInstrument[cs.Data.indexed]
    try:
        cs.Data.cadenzaOver= cs.Data.tonesFor1stInstrument[cs.Data.indexed+1]
    except: 
        cs.Data.cadenzaOver = cs.Data.tonesFor1stInstrument[cs.Data.indexed]
    Name1 = t.Tone.returnLetterName(cs.Data.cadenzaUnder)
    Octave1 = t.Tone.returnOctave(cs.Data.cadenzaUnder)
    Name2 = t.Tone.returnLetterName(cs.Data.cadenzaOver)
    Octave2 = t.Tone.returnOctave(cs.Data.cadenzaOver)
    info = f'cadenza Under: {Name1}{Octave1}    cadenza Over: {Name2}{Octave2}'
    print(info)
    db.Data.debug_log.append(info)
    cadenzaDuration = random.choice(cs.Data.beats)
    index = cs.Data.beats.index(cadenzaDuration)
    #print(f'assigned cadenza pulse in step2...maker {cadenzaDuration}')
    try:
        cs.Data.cadenzaDurationUnder = cs.Data.beats[index-1]
    except: cs.Data.cadenzaDurationUnder = cs.Data.beats[index]
    try:
        cs.Data.cadenzaDurationOver = cs.Data.beats[index+1]
    except: cs.Data.cadenzaDurationOver = cs.Data.beats[index]

    
def set_master_volume(userInteger):
    for eachObject in user_sounds.mySounds:
        Sound = gni.Note.returnSound(eachObject)
        pygame.mixer.Sound.set_volume(Sound, userInteger/10)