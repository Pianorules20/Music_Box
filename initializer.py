import instance as i, settings as s, populate_settings as ps
import random


class Initializer():
    
    #instance.voices = range(len(s.Op.instruments))

    i.tonesFor1stInstrument = s.Op.tonesFor1stInstrument

    if s.Op.tonic == 'Random':
        ps.Populate.createTonic()
    else:       
        i.tonic = s.Op.tonic
    
    indexTonic = s.Op.tonesFor1stInstrument.index(i.tonic)
    i.indexed = indexTonic
    
    if s.Op.motiveOption == 'Random':
        ps.Populate.createMotiveTones()
    else:
        i.motive = s.Op.motiveTones
        i.motiveInteger = len(i.motive)
    print(f'in initializer: length of motive: {len(i.motive)}')

    i.beats = s.Op.beats
    i.metronome = s.Op.metronome

    if s.Op.motiveRhythmOption == 'Random':
        ps.Populate.createMotiveRhythm()
    else:
        i.motiveRhythm = s.Op.motiveRhythm
    print(f'in initializer: length of motive rhythm:{len(i.motiveRhythm)} ')
    print(' ')

    if s.Op.cadenza == 'Standard':
        ps.Populate.createCadenza()
    else:
        i.cadenzaOver = s.Op.cadenzaOver
        i.cadenzaUnder = s.Op.cadenzaUnder
        i.cadenzaDurationOver = s.Op.cadenzaDurationOver
        i.cadenzaDurationUnder = s.Op.cadenzaDurationUnder
    print('')    
    
    if s.Op.notesRemaining == 'Random':
        ps.Populate.createRemainingNotes()
    else:
        i.notesRemaining = s.Op.notesRemaining
    print(f'in initializer: notes remaining {i.notesRemaining}')

    if s.Op.harmonies == 'Standard':
        ps.Populate.createHarmonies()
    else:
        i.harmony1 = s.Op.harmony1
        i.harmony2 = s.Op.harmony2
        i.harmony3 = s.Op.harmony3
        i.harmony4 = s.Op.harmony4
    
    print(s.Op.structure)

   