#populateState.py
import instance as i, mySong as my, settings as s, state

def recordState():

    state.State.localCounter += 1
    state.State.state.append(state.State.localCounter)
    
    state.State.sectionWritten.append(i.sectionWritten)
    state.State.motive.append(i.motive)
    state.State.motiveInteger.append(i.motiveInteger)
    state.State.motiveRhythm.append(i.motiveRhythm)
    state.State.instanceTonic.append(i.tonic)
    state.State.indexed.append(i.indexed)
    state.State.instanceBeats.append(i.beats)
    state.State.instanceHarmony1.append(i.harmony1)
    state.State.instanceHarmony2.append(i.harmony2)
    state.State.instanceHarmony3.append(i.harmony3)
    state.State.instanceHarmony4.append(i.harmony4)
    state.State.instanceCadenzaOver.append(i.cadenzaOver)
    state.State.instanceCadenzaUnder.append(i.cadenzaUnder)
    state.State.instanceCadenzaDurationOver.append(i.cadenzaDurationOver)
    state.State.instanceCadenzaDurationUnder.append(i.cadenzaDurationUnder)

    state.State.instanceNotesRemaining.append(i.notesRemaining)

    #the second group is from my.Trn
    state.State.finished.append(my.Trn.finished)
    state.State.meter.append(my.Trn.meter)
    state.State.currentSection.append(my.Trn.currentSection)
    state.State.TrnHarmony1.append(my.Trn.harmony1)
    state.State.TrnHarmony2.append(my.Trn.harmony2)
    state.State.TrnHarmony3.append(my.Trn.harmony3)
    state.State.TrnHarmony4.append(my.Trn.harmony4)
    state.State.transcript.append(my.Trn.transcript)
    state.State.targetStructure.append(my.Trn.targetStructure)
    state.State.generatedStructure.append(my.Trn.generatedStructure)
    state.State.newStructureInteger.append(my.Trn.newStructureInteger)
    state.State.sectionA.append(my.Trn.sectionA)
    state.State.sectionB.append(my.Trn.sectionB)
    state.State.sectionC.append(my.Trn.sectionC)
    state.State.sectionD.append(my.Trn.sectionD)
    state.State.sectionE.append(my.Trn.sectionE)

    #the third group is from s
    
    state.State.tonesFor1stInstrument.append(s.Op.tonesFor1stInstrument)
    state.State.tonesFor2ndInstrument.append(s.Op.tonesFor2ndInstrument)
    state.State.tonesFor3rdInstrument.append(s.Op.tonesFor3rdInstrument)
    state.State.tonesFor4thInstrument.append(s.Op.tonesFor4thInstrument)
    state.State.tonesFor5thInstrument.append(s.Op.tonesFor5thInstrument)
    
    state.State.metronome.append(s.Op.metronome)
    state.State.metronomeModifier.append(s.Op.metronomeModifier)

    state.State.instrument1.append(s.Op.instrument1)
    state.State.instrument2.append(s.Op.instrument2)
    state.State.instrument3.append(s.Op.instrument3)
    state.State.instrument4.append(s.Op.instrument4)
    state.State.instrument5.append(s.Op.instrument5)
    
    state.State.polyOrderList.append(s.Op.polyOrderList)
    state.State.tonic.append(s.Op.tonic)
    
    state.State.motiveOption.append(s.Op.motiveOption)
    state.State.motiveRhythmOption.append(s.Op.motiveRhythmOption)
    state.State.motiveTones.append(s.Op.motiveTones)
    state.State.motiveRhythm.append(s.Op.motiveRhythm)

    state.State.harmony1.append(s.Op.harmony1)
    state.State.harmony2.append(s.Op.harmony2)
    state.State.harmony3.append(s.Op.harmony3)
    state.State.harmony4.append(s.Op.harmony4)

    state.State.cadenza.append(s.Op.cadenza)
    state.State.cadenzaOver.append(s.Op.cadenzaOver)
    state.State.cadenzaUnder.append(s.Op.cadenzaUnder)
    state.State.cadenzaDurationOver.append(s.Op.cadenzaDurationOver)
    state.State.cadenzaDurationUnder.append(s.Op.cadenzaDurationUnder)
    
    state.State.changesBetweenSections.append(s.Op.changesBetweenSections)
    
    state.State.notesRemaining.append(s.Op.notesRemaining)

    state.rigidTempo.append(s.Op.rigidTempo)

def rewindCounter():
    state.localCounter -= 1

def advanceCounter():
    try:
        state.localCounter += 1
    except Exception as e:
        print('Cannot advance local counter in populateState()')

def goToState(n):
    i.sectionWritten = state.State.sectionWritten[n]
    i.motive = state.State.motive[n]
    i.motiveInteger = state.State.motiveInteger[n]
    i.motiveRhythm = state.State.motiveRhythm[n]
    i.tonic = state.State.instanceTonic[n]
    i.indexed = state.State.indexed[n]
    i.beats = state.State.instanceBeats[n]
    i.harmony1 = state.State.instanceHarmony1[n]
    i.harmony2 = state.State.instanceHarmony2[n]
    i.harmony3 = state.State.instanceHarmony3[n]
    i.harmony4 = state.State.instanceHarmony4[n]
    i.cadenzaOver = state.State.instanceCadenzaUnder[n]
    i.cadenzaUnder = state.State.instanceCadenzaUnder[n]
    i.cadenzaDurationOver = state.State.instanceCadenzaDurationOver[n]
    i.cadenzaDurationUnder = state.State.instanceCadenzaDurationUnder[n]
    i.notesRemaining = state.State.instanceNotesRemaining[n]

    #the second group is from mySong.Trn 'Trn'
    my.Trn.finished = state.State.finished[n]
    my.Trn.meter = state.State.meter[n]
    my.Trn.currentSection = state.State.currentSection[n]
    my.Trn.harmony1 = state.State.transcriptionHarmony1[n]
    my.Trn.harmony2 = state.State.transcriptionHarmony2[n]
    my.Trn.harmony3 = state.State.transcriptionHarmony3[n]
    my.Trn.harmony4 = state.State.transcriptionHarmony4[n]
    my.Trn.transcript = state.State.transcript[n]
    my.Trn.targetStructure = state.State.targetStructure[n]
    my.Trn.generatedStructure = state.State.generatedStructure[n]
    my.Trn.newStructureInteger = state.State.newStructureInteger[n]
    my.Trn.sectionA = state.State.sectionA[n]
    my.Trn.sectionB = state.State.sectionB[n]
    my.Trn.sectionC = state.State.sectionC[n]
    my.Trn.sectionD = state.State.sectionD[n]
    my.Trn.sectionE = state.State.sectionE[n]
    
    #the third group is from settings
    
    s.Op.tonesFor1stInstrument = state.State.tonesFor1stInstrument[n]
    s.Op.tonesFor2ndInstrument = state.State.tonesFor2ndInstrument[n]
    s.Op.tonesFor3rdInstrument = state.State.tonesFor3rdInstrument[n]
    s.Op.tonesFor4thInstrument = state.State.tonesFor4thInstrument[n]
    s.Op.tonesFor1stInstrument = state.State.tonesFor1stInstrument[n]
   
    s.Op.metronome = state.State.metronome[n]
    s.Op.metronomeModifier = state.State.metronomeModifier[n]

    s.Op.instrument1 = state.State.instrument1[n]
    s.Op.instrument2 = state.State.instrument2[n]
    s.Op.instrument3 = state.State.instrument3[n]
    s.Op.instrument4 = state.State.instrument4[n]
    s.Op.instrument5 = state.State.instrument5[n]

    s.Op.polyOrderList = state.State.polyOrderList[n]
    
    s.Op.tonic = state.State.tonic[n]
    
    s.Op.motiveOption = state.State.motiveOption[n]
    s.Op.motiveRhythmOption = state.State.motiveRhythmOption[n]
    s.Op.motiveTones = state.State.motiveTones[n]
    s.Op.motiveRhythm = state.State.motiveRhythm[n]

    s.Op.harmony1 = state.State.harmony1[n]
    s.Op.harmony2 = state.State.harmony2[n]
    s.Op.harmony3 = state.State.harmony3[n]
    s.Op.harmony4 = state.State.harmony4[n]
    
    s.Op.cadenza = state.State.cadenza[n]
    s.Op.cadenzaOver = state.State.cadenzaOver[n]
    s.Op.cadenzaUnder = state.State.cadenzaUnder[n]
    s.Op.cadenzaDurationOver = state.State.CadenzaDurationOver[n]
    s.Op.cadenzaDurationUnder = state.State.cadenzaDurationUnder[n]
    
    s.Op.changesBetweenSections = state.State.changesBetweenSections[n]
    
    s.Op.notesRemaining = state.State.notesRemaining[n]
    
    s.Op.rigidTempo = state.State.rigidTempo[n]