#populateState.py
import current_section as i, my_song as m_s, settings as s, state, debug as db

def recordState():

    '''ranger = len(state.Data.total_data) - 1  #!!!!!
    for eachData in state.Data.total_data:
        state.Data.total_data[eachData]'''

    state.Data.localCounter += 1
    state.Data.state.append(state.Data.localCounter)
    
    state.Data.sectionWritten.append(i.Data.sectionWritten)
    state.Data.motive.append(i.Data.motive)
    state.Data.motiveInteger.append(i.Data.motiveInteger)
    state.Data.motiveRhythm.append(i.Data.motiveRhythm)
    state.Data.instanceTonic.append(i.Data.tonic)
    state.Data.indexed.append(i.Data.indexed)
    state.Data.instanceBeats.append(i.Data.beats)
    state.Data.instanceHarmony1.append(i.Data.harmony1)
    state.Data.instanceHarmony2.append(i.Data.harmony2)
    state.Data.instanceHarmony3.append(i.Data.harmony3)
    state.Data.instanceHarmony4.append(i.Data.harmony4)
    state.Data.instanceCadenzaOver.append(i.Data.cadenzaOver)
    state.Data.instanceCadenzaUnder.append(i.Data.cadenzaUnder)
    state.Data.instanceCadenzaDurationOver.append(i.Data.cadenzaDurationOver)
    state.Data.instanceCadenzaDurationUnder.append(i.Data.cadenzaDurationUnder)

    state.Data.instanceNotesRemaining.append(i.Data.notesRemaining)

    #the second group is from my.Trn
    state.Data.finished.append(m_s.Data.finished)
    state.Data.meter.append(m_s.Data.meter)
    state.Data.currentSection.append(m_s.Data.currentSection)
    state.Data.TrnHarmony1.append(m_s.Data.harmony1)
    state.Data.TrnHarmony2.append(m_s.Data.harmony2)
    state.Data.TrnHarmony3.append(m_s.Data.harmony3)
    state.Data.TrnHarmony4.append(m_s.Data.harmony4)
    state.Data.transcript.append(m_s.Data.transcript)
    state.Data.targetStructure.append(m_s.Data.targetStructure)
    state.Data.generatedStructure.append(m_s.Data.generatedStructure)
    state.Data.newStructureInteger.append(m_s.Data.newStructureInteger)
    state.Data.sectionA.append(m_s.Data.sectionA)
    state.Data.sectionB.append(m_s.Data.sectionB)
    state.Data.sectionC.append(m_s.Data.sectionC)
    state.Data.sectionD.append(m_s.Data.sectionD)
    state.Data.sectionE.append(m_s.Data.sectionE)

    #the third group is from s
    
    state.Data.tonesFor1stInstrument.append(s.Data.tonesFor1stInstrument)
    state.Data.tonesFor2ndInstrument.append(s.Data.tonesFor2ndInstrument)
    state.Data.tonesFor3rdInstrument.append(s.Data.tonesFor3rdInstrument)
    state.Data.tonesFor4thInstrument.append(s.Data.tonesFor4thInstrument)
    state.Data.tonesFor5thInstrument.append(s.Data.tonesFor5thInstrument)
    
    state.Data.metronome.append(s.Data.metronome)
    state.Data.metronomeModifier.append(s.Data.metronomeModifier)

    state.Data.instrument1.append(s.Data.instrument1)
    state.Data.instrument2.append(s.Data.instrument2)
    state.Data.instrument3.append(s.Data.instrument3)
    state.Data.instrument4.append(s.Data.instrument4)
    state.Data.instrument5.append(s.Data.instrument5)
    
    state.Data.polyOrderList.append(s.Data.polyOrderList)
    state.Data.tonic.append(s.Data.tonic)
    
    state.Data.motiveOption.append(s.Data.motiveOption)
    state.Data.motiveRhythmOption.append(s.Data.motiveRhythmOption)
    state.Data.motiveTones.append(s.Data.motiveTones)
    state.Data.motiveRhythm.append(s.Data.motiveRhythm)

    state.Data.harmony1.append(s.Data.harmony1)
    state.Data.harmony2.append(s.Data.harmony2)
    state.Data.harmony3.append(s.Data.harmony3)
    state.Data.harmony4.append(s.Data.harmony4)

    state.Data.cadenza.append(s.Data.cadenza)
    state.Data.cadenzaOver.append(s.Data.cadenzaOver)
    state.Data.cadenzaUnder.append(s.Data.cadenzaUnder)
    state.Data.cadenzaDurationOver.append(s.Data.cadenzaDurationOver)
    state.Data.cadenzaDurationUnder.append(s.Data.cadenzaDurationUnder)
    
    state.Data.changesBetweenSections.append(s.Data.changesBetweenSections)
    
    state.Data.notesRemaining.append(s.Data.notesRemaining)

    state.Data.rigidTempo.append(s.Data.rigidTempo)

    state.Data.debug_log = db.Data.debug_log # check this code for accuracy

def rewindCounter():
    state.Data.localCounter -= 1

def advanceCounter():
    try:
        state.Data.localCounter += 1
    except Exception as e:
        info = 'Cannot advance local counter in populateState()'
        print(info)
        #db.Data.debug_log.append(info)

def goToState(n):
    i.Data.sectionWritten = state.Data.sectionWritten[n]
    i.Data.motive = state.Data.motive[n]
    i.Data.motiveInteger = state.Data.motiveInteger[n]
    i.Data.motiveRhythm = state.Data.motiveRhythm[n]
    i.Data.tonic = state.Data.instanceTonic[n]
    i.Data.indexed = state.Data.indexed[n]
    i.Data.beats = state.Data.instanceBeats[n]
    i.Data.harmony1 = state.Data.instanceHarmony1[n]
    i.Data.harmony2 = state.Data.instanceHarmony2[n]
    i.Data.harmony3 = state.Data.instanceHarmony3[n]
    i.Data.harmony4 = state.Data.instanceHarmony4[n]
    i.Data.cadenzaOver = state.Data.instanceCadenzaUnder[n]
    i.Data.cadenzaUnder = state.Data.instanceCadenzaUnder[n]
    i.Data.cadenzaDurationOver = state.Data.instanceCadenzaDurationOver[n]
    i.Data.cadenzaDurationUnder = state.Data.instanceCadenzaDurationUnder[n]
    i.Data.notesRemaining = state.Data.instanceNotesRemaining[n]

    #the second group is from mySong.Data
    m_s.Data.finished = state.Data.finished[n]
    m_s.Data.meter = state.Data.meter[n]
    m_s.Data.currentSection = state.Data.currentSection[n]
    m_s.Data.harmony1 = state.Data.transcriptionHarmony1[n]
    m_s.Data.harmony2 = state.Data.transcriptionHarmony2[n]
    m_s.Data.harmony3 = state.Data.transcriptionHarmony3[n]
    m_s.Data.harmony4 = state.Data.transcriptionHarmony4[n]
    m_s.Data.transcript = state.Data.transcript[n]
    m_s.Data.targetStructure = state.Data.targetStructure[n]
    m_s.Data.generatedStructure = state.Data.generatedStructure[n]
    m_s.Data.newStructureInteger = state.Data.newStructureInteger[n]
    m_s.Data.sectionA = state.Data.sectionA[n]
    m_s.Data.sectionB = state.Data.sectionB[n]
    m_s.Data.sectionC = state.Data.sectionC[n]
    m_s.Data.sectionD = state.Data.sectionD[n]
    m_s.Data.sectionE = state.Data.sectionE[n]
    
    #the third group is from settings
    
    s.Data.tonesFor1stInstrument = state.Data.tonesFor1stInstrument[n]
    s.Data.tonesFor2ndInstrument = state.Data.tonesFor2ndInstrument[n]
    s.Data.tonesFor3rdInstrument = state.Data.tonesFor3rdInstrument[n]
    s.Data.tonesFor4thInstrument = state.Data.tonesFor4thInstrument[n]
    s.Data.tonesFor1stInstrument = state.Data.tonesFor1stInstrument[n]
   
    s.Data.metronome = state.Data.metronome[n]
    s.Data.metronomeModifier = state.Data.metronomeModifier[n]

    s.Data.instrument1 = state.Data.instrument1[n]
    s.Data.instrument2 = state.Data.instrument2[n]
    s.Data.instrument3 = state.Data.instrument3[n]
    s.Data.instrument4 = state.Data.instrument4[n]
    s.Data.instrument5 = state.Data.instrument5[n]

    s.Data.polyOrderList = state.Data.polyOrderList[n]
    
    s.Data.tonic = state.Data.tonic[n]
    
    s.Data.motiveOption = state.Data.motiveOption[n]
    s.Data.motiveRhythmOption = state.Data.motiveRhythmOption[n]
    s.Data.motiveTones = state.Data.motiveTones[n]
    s.Data.motiveRhythm = state.Data.motiveRhythm[n]

    s.Data.harmony1 = state.Data.harmony1[n]
    s.Data.harmony1 = state.Data.harmony1[n]
    s.Data.harmony2 = state.Data.harmony2[n]
    s.Data.harmony3 = state.Data.harmony3[n]
    s.Data.harmony4 = state.Data.harmony4[n]
    
    s.Data.cadenza = state.Data.cadenza[n]
    s.Data.cadenzaOver = state.Data.cadenzaOver[n]
    s.Data.cadenzaUnder = state.Data.cadenzaUnder[n]
    s.Data.cadenzaDurationOver = state.Data.CadenzaDurationOver[n]
    s.Data.cadenzaDurationUnder = state.Data.cadenzaDurationUnder[n]
    
    s.Data.changesBetweenSections = state.Data.changesBetweenSections[n]
    
    s.Data.notesRemaining = state.Data.notesRemaining[n]
    
    s.Data.rigidTempo = state.Data.rigidTempo[n]

