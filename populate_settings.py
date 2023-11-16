#populates.py
import settings as s, instance as i, random, tones, sounds, pygame, generate_notes_interface

class Populate():
    
    def createRemainingNotes():
        
        rando = random.randint(40, 100)
        i.notesRemaining = rando
        
    def createTonic():
        print(' ')
        rando = random.choice(s.Op.tonesFor1stInstrument)
        i.tonic = rando
        Name = tones.Tone.returnLetterName(rando)
        Octave = tones.Tone.returnOctave(rando)
        print(f'Tonic: {Name}{Octave}')
        
    def createMotiveTones():
        print(' ')
        i.motive = []
        rando = random.randint(2, 13)       
        i.motiveInteger = rando
        for eachIndex in range(i.motiveInteger):
            new = random.choice(s.Op.tonesFor1stInstrument)
            i.motive.append(new)
        motive = []
        for eachObj in i.motive:
            Name = tones.Tone.returnLetterName(eachObj)
            motive.append(Name)
            Octave = str(tones.Tone.returnOctave(eachObj))
            motive.append(Octave)
            motive.append(' ')
        print(f'newly created motive')
        print(*motive, sep = '')
        print('')

    def createMotiveRhythm():
        print(' ')
        i.motiveRhythm = []
        for eachIndex in i.motive:
            rando = random.choice(i.beats)
            newDuration = rando     
            i.motiveRhythm.append(newDuration)
        print(f'in populates... motiveRhythm {i.motiveRhythm}')
        print(' ')
    
    def createHarmonies():

        try:
            i.harmony1 = i.tonesFor1stInstrument[i.indexed+2]  #adding integers
        except:
            i.harmony1 = i.tonesFor1stInstrument[i.indexed-5]

        try:
            i.harmony2 = i.tonesFor1stInstrument[i.indexed+3]
        except:
            i.harmony2 = i.tonesFor1stInstrument[i.indexed-4]
        try:
            i.harmony3 = i.tonesFor1stInstrument[i.indexed+4]
        except:
            i.harmony3 = i.tonesFor1stInstrument[i.indexed-3]
        try:
            i.harmony4 = i.tonesFor1stInstrument[i.indexed+5]
        except:
            i.harmony4 = i.tonesFor1stInstrument[i.indexed-2]
    
    def createCadenza():
         
        try:
            i.cadenzaUnder = i.tonesFor1stInstrument[i.indexed-1]
        except: 
            i.cadenzaUnder = i.tonesFor1stInstrument[i.indexed]
        try:
            i.cadenzaOver= i.tonesFor1stInstrument[i.indexed+1]
        except: 
            i.cadenzaOver = i.tonesFor1stInstrument[i.indexed]
        Name1 = tones.Tone.returnLetterName(i.cadenzaUnder)
        Octave1 = tones.Tone.returnOctave(i.cadenzaUnder)
        Name2 = tones.Tone.returnLetterName(i.cadenzaOver)
        Octave2 = tones.Tone.returnOctave(i.cadenzaOver)
        print(f'cadenza Under: {Name1}{Octave1}    cadenza Over: {Name2}{Octave2}')
        cadenzaDuration = random.choice(i.beats)
        index = i.beats.index(cadenzaDuration)
        #print(f'assigned cadenza pulse in step2...maker {cadenzaDuration}')
        try:
            i.cadenzaDurationUnder = i.beats[index-1]
        except: i.cadenzaDurationUnder = i.beats[index]
        try:
            i.cadenzaDurationOver = i.beats[index+1]
        except: i.cadenzaDurationOver = i.beats[index]

    
    def set_master_volume(userInteger):
        for eachObject in sounds.mySounds:
            Sound = generate_notes_interface.Creation.returnSound(eachObject)
            pygame.mixer.Sound.set_volume(Sound, userInteger/10)
