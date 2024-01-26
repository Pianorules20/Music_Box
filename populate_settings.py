#pDataulates.py
import settings as s, instance as i, random, tones as t, sounds, pygame, gni, debug as db

def createRemainingNotes():
    
    rando = random.randint(40, 120)
    i.Data.notesRemaining = rando
        
    print(' ')
    rando = random.choice(s.Data.tonesFor1stInstrument)
    i.Data.tonic = rando
    Name = t.Tone.returnLetterName(rando)
    Octave = t.Tone.returnOctave(rando)
    info = print(f'Tonic: {Name}{Octave}')      
    db.Data.debug_log.append(info)                           
        
def create_tonic():
    print(' ')
    rando = random.choice(s.Data.tonesFor1stInstrument)
    i.Data.tonic = rando
    info = print(f'tonic is {i.Data.tonic}')
    db.Data.debug_log.append(info)


def createMotiveTones():
    print(' ')
    i.Data.motive = []
    rando = random.randint(2, 13)       
    i.Data.motiveInteger = rando
    for eachIndex in range(i.Data.motiveInteger):
        new = random.choice(s.Data.tonesFor1stInstrument)
        i.Data.motive.append(new)
    motive = []
    for eachObj in i.Data.motive:
        Name = t.Tone.returnLetterName(eachObj)
        motive.append(Name)
        Octave = str(t.Tone.returnOctave(eachObj))
        motive.append(Octave)
        motive.append(' ')
    print(f'newly created motive')
    print(*motive, sep = '')
    print('')

def createMotiveRhythm():
    print(' ')
    i.Data.motiveRhythm = []
    for eachIndex in i.Data.motive:
        rando = random.choice(i.Data.beats)
        newDuration = rando     
        i.Data.motiveRhythm.append(newDuration)
    print(f'in populate_settings... motiveRhythm {i.Data.motiveRhythm}')
    print(' ')

def createHarmonies():

    try:
        i.Data.harmony1 = i.Data.tonesFor1stInstrument[i.Data.indexed+2]  #adding integers
    except:
        i.Data.harmony1 = i.Data.tonesFor1stInstrument[i.Data.indexed-5]

    try:
        i.Data.harmony2 = i.Data.tonesFor1stInstrument[i.Data.indexed+3]
    except:
        i.Data.harmony2 = i.Data.tonesFor1stInstrument[i.Data.indexed-4]
    try:
        i.Data.harmony3 = i.Data.tonesFor1stInstrument[i.Data.indexed+4]
    except:
        i.Data.harmony3 = i.Data.tonesFor1stInstrument[i.Data.indexed-3]
    try:
        i.Data.harmony4 = i.Data.tonesFor1stInstrument[i.Data.indexed+5]
    except:
        i.Data.harmony4 = i.Data.tonesFor1stInstrument[i.Data.indexed-2]
    
def createCadenza():
        
    try:
        i.Data.cadenzaUnder = i.Data.tonesFor1stInstrument[i.Data.indexed-1]
    except: 
        i.Data.cadenzaUnder = i.Data.tonesFor1stInstrument[i.Data.indexed]
    try:
        i.Data.cadenzaOver= i.Data.tonesFor1stInstrument[i.Data.indexed+1]
    except: 
        i.Data.cadenzaOver = i.Data.tonesFor1stInstrument[i.Data.indexed]
    Name1 = t.Tone.returnLetterName(i.Data.cadenzaUnder)
    Octave1 = t.Tone.returnOctave(i.Data.cadenzaUnder)
    Name2 = t.Tone.returnLetterName(i.Data.cadenzaOver)
    Octave2 = t.Tone.returnOctave(i.Data.cadenzaOver)
    print(f'cadenza Under: {Name1}{Octave1}    cadenza Over: {Name2}{Octave2}')
    cadenzaDuration = random.choice(i.Data.beats)
    index = i.Data.beats.index(cadenzaDuration)
    #print(f'assigned cadenza pulse in step2...maker {cadenzaDuration}')
    try:
        i.Data.cadenzaDurationUnder = i.Data.beats[index-1]
    except: i.Data.cadenzaDurationUnder = i.Data.beats[index]
    try:
        i.Data.cadenzaDurationOver = i.Data.beats[index+1]
    except: i.Data.cadenzaDurationOver = i.Data.beats[index]

    
def set_master_volume(userInteger):
    for eachObject in sounds.mySounds:
        Sound = gni.Creation.returnSound(eachObject)
        pygame.mixer.Sound.set_volume(Sound, userInteger/10)