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

        
    Count.copy = my.Trn.transcript #this is a list inside of a list - it is the total song
    #print(f' {len(Count.copy)} in pni.Count.populate()')  #breadcrumb

    if len(Count.copy) > 0:
        Count.thisSection = Count.copy[0] #separating the sections/lists in the copy
    else:
        Count.thisSection = Count.copy #this is the final section for depopulation

    print(f' in pni.populate mySong.Trn.transcript {len(my.Trn.transcript)}')  #breadcrumb
    print('why is mySong transcribed incorrectly?')
    Count.sectionInteger = len(Count.copy)
    
    Count.counter = len(Count.thisSection)
    print(f'in pni.populate...Count.counter {Count.counter}')

    Count.populate = False

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
    print('in pni class Inc') #breadcrumb
    sounds = []
    currentPlot = []
    for eachNote in currentPlot:
        sounds.append(gni.returnSound(eachNote))

def createIncrement():
    print('in pni createIncrement')  #breadcrumb
    inc = Inc()
    if len(Inc.sounds) > 0: 
        print('sound plot created')
    else:
        print('empty plot created')
    play.Player.recording.append(inc)