import instance as i, settings as s, populate_settings as ps
import random


class Initializer():
    
    #instance.voices = range(len(s.Data.instruments))

    i.Data.tonesFor1stInstrument = s.Data.tonesFor1stInstrument

    if s.Data.tonic == 'Random':
        ps.createTonic()
    else:       
        i.Data.tonic = s.Data.tonic
    
    indexTonic = s.Data.tonesFor1stInstrument.index(i.Data.tonic)
    i.Data.indexed = indexTonic
    
    if s.Data.motiveOption == 'Random':
        ps.createMotiveTones()
    else:
        i.Data.motive = s.Data.motiveTones
        i.Data.motiveInteger = len(i.Data.motive)
    print(f'in initializer: length of motive: {len(i.Data.motive)}')

    i.Data.beats = s.Data.beats
    i.Data.metronome = s.Data.metronome

    if s.Data.motiveRhythmOption == 'Random':
        ps.createMotiveRhythm()
    else:
        i.Data.motiveRhythm = s.Data.motiveRhythm
    print(f'in initializer: length of motive rhythm:{len(i.Data.motiveRhythm)} ')
    print(' ')

    if s.Data.cadenza == 'Standard':
        ps.createCadenza()
    else:
        i.Data.cadenzaOver = s.Data.cadenzaOver
        i.Data.cadenzaUnder = s.Data.cadenzaUnder
        i.Data.cadenzaDurationOver = s.Data.cadenzaDurationOver
        i.Data.cadenzaDurationUnder = s.Data.cadenzaDurationUnder
    print('')    
    
    if s.Data.notesRemaining == 'Random':
        ps.createRemainingNotes()
    else:
        i.Data.notesRemaining = s.Data.notesRemaining
    print(f'in initializer: notes remaining {i.Data.notesRemaining}')

    if s.Data.harmonies == 'Standard':
        ps.createHarmonies()
    else:
        i.Data.harmony1 = s.Data.harmony1
        i.Data = s.Data.harmony2
        i.Data.harmony3 = s.Data.harmony3
        i.Data.harmony4 = s.Data.harmony4
    
    print(s.Data.structure)