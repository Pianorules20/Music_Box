#instance.py
import settings as s, mySong as my

class Data():

    current_section = []
    sectionWritten = False

    tonesFor1stInstrument = s.Data.tonesFor1stInstrument
    tonesFor2ndInstrument = s.Data.tonesFor2ndInstrument
    tonesFor3rdInstrument = s.Data.tonesFor3rdInstrument
    tonesFor4thInstrument = s.Data.tonesFor4thInstrument
    tonesFor5thInstrument = s.Data.tonesFor5thInstrument
    instruments = [tonesFor1stInstrument, tonesFor2ndInstrument, tonesFor3rdInstrument, \
                tonesFor4thInstrument, tonesFor5thInstrument]

    voices = int(0) #does not reset with instance reset

    motive = s.Data.motiveTones
    motiveInteger = len(s.Data.motiveTones)
    motiveRhythm = s.Data.motiveRhythm

    tonic = s.Data.tonesFor1stInstrument[0]
    indexed = int(2)

    beats = s.Data.beats

    metronome = int(1)

    harmony1 = s.Data.harmony1
    harmony2 = s.Data.harmony2
    harmony3 = s.Data.harmony3
    harmony4 = s.Data.harmony4
    harmonies = [harmony1, harmony2, harmony3, harmony4]

    cadenzaOver = s.Data.cadenzaOver
    cadenzaUnder = s.Data.cadenzaUnder
    cadenzaDurationOver = s.Data.cadenzaDurationOver
    cadenzaDurationUnder = s.Data.cadenzaDurationUnder

    notesRemaining = int(1)

def reset_instance():
    print('in mySongs.Data.reset()')
    # i.sectionWritten = False
    Data.motive = []
    Data.motiveInteger = int(1)
    Data.motiveRhythm = []
    Data.tonic = int(0)
    Data.harmony1 = int(2)
    Data.harmony2 = int(3)
    Data.harmony3 = int(4)
    Data.harmony4 = int(5)
    Data.notesRemaining = int(s.Data.notesRemaining)
    Data.sectionWritten = False
    Data.currentSection = []

def transcribe_section():
    my.Data.current_section = Data.current_section