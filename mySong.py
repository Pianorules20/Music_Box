#mySong.py
import settings as s, random, initializer as init, debug as db

class Data(): #'Trn' stands for 'Transcription'
    song_finished = False
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

#def initializer():
#    init.initialize()
def flip_finished():
    Data.song_finished = not Data.song_finished
    info = f'Data.song_finished = {Data.song_finished}'
    print(info)
    db.Data.debug_log.append(info)

def createStructure():
    Data.newStructureInteger = random.randint(1,5)

def nextInstrument():
    s.Data.createRemainingNotes()
    '''dev warning!!! watchout for me!'''

#def advance_meter():
#    Data.meter -= (s.Data.metronome/s.Data.metronomeModifier)
    
#def reset_meter():
#    Data.meter = int(0)

def reset_transcript(): # watch out for me!  Trn.finished...
    flip_finished()
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
    info = 'in mySong.reset_transcript()'
    print(info)
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