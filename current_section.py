#instance.py
import settings as s, my_song as m_s, tones as t
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
    tonesFor6thVoice = s.Data.tonesFor6thVoice
    volumeFor6thVoice = s.Data.volumeFor6thVoice
    tonesFor7thVoice = s.Data.tonesFor7thVoice
    volumeFor7thVoice = s.Data.volumeFor7thVoice
    tonesFor8thVoice = s.Data.tonesFor8thVoice
    volumeFor8thVoice = s.Data.volumeFor8thVoice
    tonesFor9thVoice = s.Data.tonesFor9thVoice
    volumeFor9thVoice = s.Data.volumeFor9thVoice
    tonesFor10thVoice = s.Data.tonesFor10thVoice
    volumeFor10thVoice = s.Data.volumeFor10thVoice
    voices_list = [tonesFor1stVoice, tonesFor2ndVoice, tonesFor3rdVoice, tonesFor4thVoice, tonesFor5thVoice, \
                   tonesFor6thVoice, tonesFor7thVoice, tonesFor8thVoice, tonesFor9thVoice, tonesFor10thVoice]

    #voices = int(0) #does not reset with instance reset

    motive = s.Data.motiveTones
    motiveInteger = len(s.Data.motiveTones)
    motiveRhythm = s.Data.motiveRhythm

    tonic = s.Data.tonesFor1stVoice[0]
    indexed = int(2)

    beats = s.Data.beats

    #metronome = int(1)

    harmony1:t.Tone = s.Data.harmony1
    harmony2 = s.Data.harmony2
    harmony3 = s.Data.harmony3
    harmony4 = s.Data.harmony4
    harmonies = [harmony1, harmony2, harmony3, harmony4]

    cadenzaOver = s.Data.cadenzaOver
    cadenzaUnder = s.Data.cadenzaUnder
    cadenzaDurationOver = s.Data.cadenzaDurationOver
    cadenzaDurationUnder = s.Data.cadenzaDurationUnder

    notesRemaining:int = s.Data.notesRemaining

def reset_instance():
    print('in current_section.reset_instance(),_called_by_post_production.py_')
    
    Data.current_section = []
    Data.sectionWritten = False

    Data.tonesFor1stVoice = s.Data.tonesFor1stVoice
    Data.volumeFor1stVoice = s.Data.volumeFor1stVoice
    Data.tonesFor2ndVoice = s.Data.tonesFor2ndVoice
    Data.volumeFor2ndVoice = s.Data.volumeFor2ndVoice
    Data.tonesFor3rdVoice = s.Data.tonesFor3rdVoice
    Data.volumeFor3rdVoice = s.Data.volumeFor3rdVoice
    Data.tonesFor4thVoice = s.Data.tonesFor4thVoice
    Data.volumeFor4thVoice = s.Data.volumeFor4thVoice
    Data.tonesFor5thVoice = s.Data.tonesFor5thVoice
    Data.volumeFor5thVoice = s.Data.volumeFor5thVoice
    Data.tonesFor6thVoice = s.Data.tonesFor6thVoice
    Data.volumeFor6thVoice = s.Data.volumeFor6thVoice
    Data.tonesFor7thVoice = s.Data.tonesFor7thVoice
    Data.volumeFor7thVoice = s.Data.volumeFor7thVoice
    Data.tonesFor8thVoice = s.Data.tonesFor8thVoice
    Data.volumeFor8thVoice = s.Data.volumeFor8thVoice
    Data.tonesFor9thVoice = s.Data.tonesFor9thVoice
    Data.volumeFor9thVoice = s.Data.volumeFor9thVoice
    Data.tonesFor10thVoice = s.Data.tonesFor10thVoice
    Data.volumeFor10thVoice = s.Data.volumeFor10thVoice
    Data.voices_list = [Data.tonesFor1stVoice, Data.tonesFor2ndVoice, Data.tonesFor3rdVoice, \
                Data.tonesFor4thVoice, Data.tonesFor5thVoice, Data.tonesFor6thVoice, Data.tonesFor7thVoice,\
                    Data.tonesFor8thVoice, Data.tonesFor9thVoice, Data.tonesFor10thVoice]
    Data.volumes_list = [Data.volumeFor1stVoice, Data.volumeFor2ndVoice, Data.volumeFor3rdVoice, Data.volumeFor4thVoice, \
                        Data.volumeFor5thVoice, Data.volumeFor6thVoice, Data.volumeFor7thVoice, Data.volumeFor8thVoice, \
                        Data.volumeFor9thVoice, Data.volumeFor10thVoice]
    #Data.voices = int(0) #does not reset with instance reset

    Data.motive = s.Data.motiveTones
    Data.motiveInteger = len(s.Data.motiveTones)
    Data.motiveRhythm = s.Data.motiveRhythm

    Data.tonic = s.Data.tonesFor1stVoice[0]
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

    Data.notesRemaining = s.Data.notesRemaining
    
def transcribe_voice():

    info = 'in c_s.transcribe_voice().  resetting c_s current_section'
    print(info)
    #db.Data.debug_log.append(info)

    for eachNote in Data.current_section:
        m_s.Data.current_section.append(eachNote)
    Data.current_section = []