#instance.py
import settings as s, mySong as my, current_section as cs
class Data():

    current_section = []
    sectionWritten = False

    tonesFor1stInstrument = s.Data.tonesFor1stInstrument
    volumeFor1stInstrument = s.Data.volumeFor1stInstrument
    tonesFor2ndInstrument = s.Data.tonesFor2ndInstrument
    volumeFor2ndInstrument = s.Data.volumeFor2ndInstrument
    tonesFor3rdInstrument = s.Data.tonesFor3rdInstrument
    volumeFor3rdInstrument = s.Data.volumeFor3rdInstrument
    tonesFor4thInstrument = s.Data.tonesFor4thInstrument
    volumeFor4thInstrument = s.Data.volumeFor4thInstrument
    tonesFor5thInstrument = s.Data.tonesFor5thInstrument
    volumeFor5thInstrument = s.Data.volumeFor5thInstrument
    instruments = [tonesFor1stInstrument, tonesFor2ndInstrument, tonesFor3rdInstrument, \
                tonesFor4thInstrument, tonesFor5thInstrument]

    #voices = int(0) #does not reset with instance reset

    motive = s.Data.motiveTones
    motiveInteger = len(s.Data.motiveTones)
    motiveRhythm = s.Data.motiveRhythm

    tonic = s.Data.tonesFor1stInstrument[0]
    indexed = int(2)

    beats = s.Data.beats

    #metronome = int(1)

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
    print('in current_section.reset_instance(),_called_by_post_production.py_')
    
    Data.current_section = []
    Data.sectionWritten = False

    Data.tonesFor1stInstrument = s.Data.tonesFor1stInstrument
    Data.volumeFor1stInstrument = s.Data.volumeFor1stInstrument
    Data.tonesFor2ndInstrument = s.Data.tonesFor2ndInstrument
    Data.volumeFor2ndInstrument = s.Data.volumeFor2ndInstrument
    Data.tonesFor3rdInstrument = s.Data.tonesFor3rdInstrument
    Data.volumeFor3rdInstrument = s.Data.volumeFor3rdInstrument
    Data.tonesFor4thInstrument = s.Data.tonesFor4thInstrument
    Data.volumeFor4thInstrument = s.Data.volumeFor4thInstrument
    Data.tonesFor5thInstrument = s.Data.tonesFor5thInstrument
    Data.volumeFor5thInstrument = s.Data.volumeFor5thInstrument
    Data.instruments = [Data.tonesFor1stInstrument, Data.tonesFor2ndInstrument, Data.tonesFor3rdInstrument, \
                Data.tonesFor4thInstrument, Data.tonesFor5thInstrument]

    #Data.voices = int(0) #does not reset with instance reset

    Data.motive = s.Data.motiveTones
    Data.motiveInteger = len(s.Data.motiveTones)
    Data.motiveRhythm = s.Data.motiveRhythm

    Data.tonic = s.Data.tonesFor1stInstrument[0]
    Data.indexed = int(2)

    Data.beats = s.Data.beats

    #metronome = int(1)

    Data.harmony1 = s.Data.harmony1
    Data.harmony2 = s.Data.harmony2
    Data.harmony3 = s.Data.harmony3
    Data.harmony4 = s.Data.harmony4
    Data.harmonies = [Data.harmony1, Data.harmony2, Data.harmony3, Data.harmony4]

    Data.cadenzaOver = s.Data.cadenzaOver
    Data.cadenzaUnder = s.Data.cadenzaUnder
    Data.cadenzaDurationOver = s.Data.cadenzaDurationOver
    Data.cadenzaDurationUnder = s.Data.cadenzaDurationUnder

    Data.notesRemaining = int(1)
    
def transcribe_section():

    for eachNote in Data.current_section:
        my.Data.current_section.append(eachNote)