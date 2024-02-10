#instance.py
import settings as s, mySong as m_s, current_section as cs
class Data():

    current_section = []
    sectionWritten = False

    tonesFor1stVoice = s.Data.tonesFor1stVoice
    volumeFor1stVoice = s.Data.volumeFor1stVoice
    tonesFor2ndVoice = s.Data.tonesFor2ndVoice
    volumeFor2ndVoice = s.Data.volumeFor2ndVoice
    tonesFor3rdVoice = s.Data.tonesFor3rdVoice
    volumeFor3rdVoice = s.Data.volumeFor3rdVoice
    tonesFor4thVoice = s.Data.tonesFor4thVoice
    volumeFor4thVoice = s.Data.volumeFor4thVoice
    tonesFor5thVoice = s.Data.tonesFor5thVoice
    volumeFor5thVoice = s.Data.volumeFor5thVoice
    voices_list = [tonesFor1stVoice, tonesFor2ndVoice, tonesFor3rdVoice, \
                tonesFor4thVoice, tonesFor5thVoice]

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
    
def transcribe_voice():

    for eachNote in Data.current_section:
        m_s.Data.current_section.append(eachNote)
        Data.current_section = []