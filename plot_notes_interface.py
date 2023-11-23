# plot_notes_interface.py
import playback as play, generate_notes_interface as gni, mySong as my, gatekeeper, tones as t


class I(): #'I' stands for 'Interface'

    transcriptCopy = []
    sectionInteger = int(0)
    currentSection = int(0) 
    noteCounter = int(0)
    populateMe = True
    thisSection = []    
    currentPlot = [] #this is the fundamental unit that will be tracked
    currentSounds = [] 
    '''for eachNote in currentPlot:
        sounds.append(gni.returnSound(eachNote))'''
    
class Increment(): # stands for 'Increment'

    #print('in pni class Inc') #breadcrumb 
    def __init__(self, sounds):

        self.sounds = sounds


def createIncrement(sounds):
    
    print('in pni createIncrement')  #breadcrumb
    myPlot = Increment(sounds = sounds)
    if len(myPlot.sounds) > 0: 
        print('sound plot created')
    else:
        print('empty plot created')
    play.Player.recording.append(myPlot)

def populate():
        
    I.transcriptCopy = my.Trn.transcript #this is a list inside of a list - it is the total song
    #print(f' {len(Count.copy)} in pni.Count.populate()')  #breadcrumb

    if len(I.transcriptCopy) > 0:  #counting the sections in the transcript
        I.thisSection = I.transcriptCopy[0] #separating the sections/lists in the copy
    else:
        I.thisSection = I.transcriptCopy #this is the final section for depopulation

    print(f' in pni.populate transcript copy {len(I.transcriptCopy)}')
    print(I.transcriptCopy)  #breadcrumb
    print('why is mySong transcribed incorrectly?')
    I.sectionInteger = len(I.thisSection)
    I.noteCounter = len(I.thisSection)
    print(f'in pni.populate...I.counter {I.noteCounter}')
    I.populateMe = False

def advance():
    if I.currentSection < I.sectionCounter:
        I.currentSection += 1
    else:
        gatekeeper.Gate.current = 'playback'

def resetSection():
    print('reset Section')
    I.sectionCounter = int(0)

    I.currentSection = int(0)

    I.noteCounter - int(0)

    I.populateMe = True

def resetPlot():
    print('reset plot')
    I.currentPlot = []
    I.sounds = []


def populateSounds():

    for eachNote in I.currentPlot:
        sound = t.Tone.returnSound(eachNote)
        I.currentSounds.append(sound)