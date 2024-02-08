import current_section as cs, settings as s, populate_settings as ps, debug as db
import random

class Data():
    pass

def initialize():
    
    #instance.voices = range(len(s.Data.instruments))

    cs.Data.tonesFor1stInstrument = s.Data.tonesFor1stInstrument

    if s.Data.tonic == 'Random':
        ps.create_tonic()
    else:       
        cs.Data.tonic = s.Data.tonic
    
    indexTonic = s.Data.tonesFor1stInstrument.index(cs.Data.tonic)
    cs.Data.indexed = indexTonic
    
    if s.Data.motiveOption == 'Random':
        ps.createMotiveTones()
    else:
        cs.Data.motive = s.Data.motiveTones
        cs.Data.motiveInteger = len(cs.Data.motive)
    info = f'in initializer: length of motive: {len(cs.Data.motive)}'
    print(info)
    db.Data.debug_log.append(info)

    cs.Data.beats = s.Data.beats
    cs.Data.metronome = s.Data.metronome

    if s.Data.motiveRhythmOption == 'Random':
        ps.createMotiveRhythm()
    else:
        cs.Data.motiveRhythm = s.Data.motiveRhythm
    info = f'in initializer: length of motive rhythm:{len(cs.Data.motiveRhythm)}'
    print(info)
    db.Data.debug_log.append(info)
    print(' ')

    if s.Data.cadenza == 'Standard':
        ps.createCadenza()
    else:
        cs.Data.cadenzaOver = s.Data.cadenzaOver
        cs.Data.cadenzaUnder = s.Data.cadenzaUnder
        cs.Data.cadenzaDurationOver = s.Data.cadenzaDurationOver
        cs.Data.cadenzaDurationUnder = s.Data.cadenzaDurationUnder
    print('')    
    
    if s.Data.notesRemainingOption == 'Random':
        ps.createRemainingNotes()
    else:
        cs.Data.notesRemaining = s.Data.notesRemaining
    info = f'in initializer: notes remaining {cs.Data.notesRemaining}'
    print(info)
    db.Data.debug_log.append(info)

    if s.Data.harmonies == 'Standard':
        ps.createHarmonies()
    else:
        cs.Data.harmony1 = s.Data.harmony1
        cs.Data.harmony2 = s.Data.harmony2
        cs.Data.harmony3 = s.Data.harmony3
        cs.Data.harmony4 = s.Data.harmony4
    info = f'in initializer: refer to settings.Data.structure {s.Data.structure}'
    print(info)
    db.Data.debug_log.append(info)