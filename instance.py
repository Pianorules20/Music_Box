#instance.py
import settings as s  #'Op' stands for 'options'

class Data():

    sectionWritten = False

    tonesFor1stInstrument = s.Op.tonesFor1stInstrument
    tonesFor2ndInstrument = s.Op.tonesFor2ndInstrument
    tonesFor3rdInstrument = s.Op.tonesFor3rdInstrument
    tonesFor4thInstrument = s.Op.tonesFor4thInstrument
    tonesFor5thInstrument = s.Op.tonesFor5thInstrument
    instruments = [tonesFor1stInstrument, tonesFor2ndInstrument, tonesFor3rdInstrument, \
                tonesFor4thInstrument, tonesFor5thInstrument]

    voices = int(0) #does not reset with instance reset

    motive = s.Op.motiveTones
    motiveInteger = len(s.Op.motiveTones)
    motiveRhythm = s.Op.motiveRhythm

    tonic = s.Op.tonesFor1stInstrument[0]
    indexed = int(2)

    beats = s.Op.beats

    metronome = int(1)

    harmony1 = s.Op.harmony1
    harmony2 = s.Op.harmony2
    harmony3 = s.Op.harmony3
    harmony4 = s.Op.harmony4
    harmonies = [harmony1, harmony2, harmony3, harmony4]

    cadenzaOver = s.Op.cadenzaOver
    cadenzaUnder = s.Op.cadenzaUnder
    cadenzaDurationOver = s.Op.cadenzaDurationOver
    cadenzaDurationUnder = s.Op.cadenzaDurationUnder

    notesRemaining = int(1)