# plot_notes_interface.py
import playback as play, generate_notes_interface as gni, mySong as my, gatekeeper


class Count(): #'C' stands for 'counter'

    copy = []
    sectionInteger = int(0)
    currentSection = int(0) 
    noteCounter = int(0)
    populate = True
    thisSection = []

    def populate():

        Count.copy = my.Trn.transcript #this is a list inside of a list

        Count.sectionInteger = len(Count.copy)
        
        Count.thisSection = Count.copy[0] #this is a list for depopulation 
        
        Count.counter = len(Count.thisSection)

        Count.populate != Count.populate

    def advance():
        if Count.currentSection < Count.sectionCounter:
            Count.currentSection += 1
        else:
            gatekeeper.Gate.current = 'playback'

    def reset():

        Count.sectionCounter = int(0)

        Count.currentSection = int(0)

        Count.noteCounter - int(0)

        Count.populate = True

class Inc(): # stands for 'Increment'
    
    sounds = []
    currentPlot = []
    for eachNote in currentPlot:
        sounds.append(gni.returnSound(eachNote))

def createIncrement():
    inc = Inc()
    if len(Inc.sounds) > 0: 
        print('sound plot created')
    else:
        print('empty plot created')
    play.Player.recording.append(inc)