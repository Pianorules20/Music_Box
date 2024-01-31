#mySong.py
import settings as s, random, initializer, debug as db

class Data(): #'Trn' stands for 'Transcription'
    finished = False
    meter = int(0)
    current_section = []
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
    s.Data.createRemainingNotes()

def advance_meter():
    Data.meter -= (s.Data.metronome/s.Data.metronomeModifier)
    
def reset_meter():
    Data.meter = int(0)

def reset_transcript(): # watch out for me!  Trn.finished...
    Data.finished = False
    Data.current_section = []
    Data.transcript = []
    Data.harmony1 = []
    Data.harmony2 = []
    Data.harmony3 = []
    Data.harmony4 = []
    Data.sectionA = []
    Data.sectionB = []
    Data.sectionC = []
    Data.sectionD = []
    Data.sectionE = []
    Data.generatedStructure = []
    Data.newStructureInteger = int(0)
    Data.targetStructure = []
    Data.meter = int(0)
    info = print('in mySong.reset_transcript()')
    db.Data.debug_log.append(info)

def resetSection():
    Data.currentSection = []
    
    '''def recordSection():  # watch out for me!  Trn.finished...
    for eachList in Data.currentSection:
        Data.transcript.append(Data.currentSection[eachList])'''
    #Trn.finished = True revisit this line
        
    '''def Trn():
            Trn.finished = True
            fileName = 'newFile.txt'
            fileStructure = Trn.generatedStructure
            melody = Trn.melody
            create a file that transcribes the data'''