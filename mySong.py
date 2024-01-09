#mySong.py
import settings as s, instance as i, random, initializer

class Trn(): #'Trn' stands for 'Transcription'
    finished = False
    meter = int(0)
    currentSection = []
    harmony1 = []
    harmony2 = []
    harmony3 = []
    harmony4 = []
    transcript = []
    targetStructure = []
    generatedStructure = []
    newStructureInteger = int(0)
    sectionA = []
    sectionB = []
    sectionC = []
    sectionD = []
    sectionE = []

def initializer():
    initializer.Initializer()

def createStructure():
    newStructureInteger = random.randint(1,5)

def nextInstrument():
    s.Op.createRemainingNotes()

def advance():
    Trn.Meter -= (s.Op.metronome/s.Op.metronomeModifier)

def resetInstance():
    print('in mySongs.Trn.reset()')
    # i.sectionWritten = False
    i.motive = []
    i.motiveInteger = int(1)
    i.motiveRhythm = []
    i.tonic = int(0)
    i.harmony1 = int(2)
    i.harmony2 = int(3)
    i.harmony3 = int(4)
    i.harmony4 = int(5)
    try:
        i.notesRemaining = s.Op.notesRemaining
    except:
        i.notesRemaining = s.Op.createRemainingNotes()
    i.sectionWritten = False
    Trn.currentSection = []

def resetTranscript(): # watch out for me!  Trn.finished...
    Trn.finished = False
    Trn.transcript = []
    Trn.generatedStructure = []
    Trn.newStructureInteger = int(0)
    Trn.targetStructure = []

def resetSection():
    Trn.currentSection = []
    
def recordSection():  # watch out for me!  Trn.finished...
    for eachList in Trn.currentSection:
        Trn.transcript.append(Trn.currentSection[eachList])
    #Trn.finished = True revisit this line
        
    '''def Trn():
            Trn.finished = True
            fileName = 'newFile.txt'
            fileStructure = Trn.generatedStructure
            melody = Trn.melody
            create a file that transcribes the data'''
