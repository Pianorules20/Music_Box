#state.py

class Data():
    
    #this is governing variable
    localCounter = int(-1)
    state = []

    #the first group is from instance
    sectionWritten = []

    motive = []
    motiveInteger = []
    motiveRhythm = []

    instanceTonic = []
    indexed = []

    instanceBeats = []

    instanceHarmony1 = []
    instanceHarmony2 = []     
    instanceHarmony3 = []                                                                                                                 
    instanceHarmony4 = []

    instanceCadenzaOver = []
    instanceCadenzaUnder = []
    instanceCadenzaDurationOver = []
    instanceCadenzaDurationUnder = []

    instanceNotesRemaining = []

    #the second group is from mySongs.transcription
    finished = []
    meter = []
    currentSection = []
    transcriptionHarmony1 = []
    transcriptionHarmony2 = []
    transcriptionHarmony3 = []
    transcriptionHarmony4 = []
    transcript = []
    targetStructure = []
    generatedStructure = []
    newStructureInteger = []
    sectionA = []
    sectionB = []
    sectionC = []
    sectionD = []
    sectionE = []

    #the third group is from settings
    
    tonesFor1stInstrument = []
    tonesFor2ndInstrument = []
    tonesFor3rdInstrument = []
    tonesFor4thInstrument = []
    tonesFor5thInstrument = []
    
    metronome = []
    metronomeModifier = []

    instrument1 = []
    instrument2 = []
    instrument3 = []
    instrument4 = []
    instrument5 = []
    
    polyOrderList = []
    tonic = []
    
    motiveOption = []
    motiveRhythmOption = []
    motiveTones  = [] 
    motiveRhythm = []

    harmony1 = []
    harmony2 = []
    harmony3 = []
    harmony4 = []

    cadenza = []
    cadenzaOver = []
    cadenzaUnder = []
    cadenzaDurationOver = []
    cadenzaDurationUnder = []
    
    #for best debugging change structure to another option in 'structureOptions'
    structure  = []
    
    changeSettingsBetweenSections = []
    notesRemaining = []

    rigidTempo = []

    debug_log = []

    objects = []

    total_data = []

    transfer_notes = []

def update(data, destination):
    match destination:
        case Data.transfer_notes:
            Data.transfer_notes.append(data)