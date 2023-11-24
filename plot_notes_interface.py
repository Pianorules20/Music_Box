# plot_notes_interface.py
import playback as play, gni as gni, mySong as my, gatekeeper, tones as t


class I(): #'I' stands for 'Interface'

    transcriptCopy = []
    sectionInteger = int(0)
    currentSection = int(0) 
    sectionCounts = []
    currentCounter = int(0)
    populateMe = True
    thisSection = []    
    currentPlot = [] #this is the fundamental unit that will be tracked
    currentSounds = [] 
    '''for eachNote in currentPlot:
        sounds.append(gni.returnSound(eachNote))'''
    
class Plot(): # stands for 'Increment'

    #print('in pni class Inc') #breadcrumb 

    def __init__(self, notesInternal):

        self.notesInternal = notesInternal
        
    def playNotes(self):

        for eachNote in self.notesInternal:

            sound = gni.Note.returnSound(eachNote)

            gni.Note.play(sound)



def createPlot(notesExternal):
    
    print('in pni createIncrement')  #breadcrumb
    myPlot = Plot(notesInternal = notesExternal)
    if len(myPlot.notesInternal) > 0: 
        print('sound plot created')
    else:
        print('empty plot created')
    play.Player.recording.append(myPlot)
    #count -1???

def populateNotes():
            
    for eachSection in my.Trn.transcript:
            count = len(eachSection) 
            I.sectionCounts.append(count)
            I.currentSection = I.sectionCounts[0] 
        
         #this is a list inside of a list - it is the total song
        #print(f' in pni.populate transcript copy {len(I.transcriptCopy)}')
        #print(f' in pni.populate...I.transcriptCopy {I.transcriptCopy}')  #breadcrumb
        #print('why is mySong transcribed incorrectly?')
    I.populateMe = False

def resetSection():
    print('reset Section')
    I.sectionCounter = int(0)

    I.currentSection = int(0)

    I.counter - int(0)

    I.populateMe = True

def advance():

    try:

        I.sectionInteger += 1
        
        I.currentSection = my.Trn.transcript[I.sectionInteger]
    
    except:
        
        resetSection()

        print('pni line 72...switch to playback after section advance out of range')
        gatekeeper.Gate.current = 'playback'
        


def resetPlot():
    print('reset plot')
    I.currentPlot = []
    I.sounds = []


def populateSounds():

    for eachNote in I.currentPlot:
        sound = t.Tone.returnSound(eachNote)
        I.currentSounds.append(sound)