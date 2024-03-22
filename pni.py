# pni = 'plot_notes_interface.py'
import pygame
import playback as pb, gni as gni, my_song as m_s, tones as t, debug as db, layout_playback_style as l_p

class Data():
    
    current_plot = []
    transfer_notes = True


    '''def __init__(self, Note, sound, image, rectangle):

        self.Note = Note
        self.sound = sound
        self.image = image
        self.rectangle = rectangle'''

def create_plot():
    info = 'in pni create_plot() '
    print(info)
    db.Data.debug_log = info
    if len(Data.current_plot) == 0:
        pb.Data.final_copy.append([])
    else:
        sounds = []
        for eachNote in Data.current_plot:
            sound = t.Tone.returnSound(eachNote)
            sounds.append(sound)
            pb.Data.final_copy.append(sounds)
            l_p.Data.objects.append(eachNote)


'''def create_plot():

    #info = f'pni_create_plot'
    #print(info)
    #db.Data.debug_log.append(info)

    if len(Data.current_plot) == 0:
        #info = f'empty plot'
        #print(info)
        #db.Data.debug_log.append(info)
        pb.Data.final_copy.append(None)

    else:
        for eachNote in Data.current_plot:
            sound = eachNote.sound
            image = pygame.Surface((100,100))
            rectangle = eachNote.image.get_rect()
            rectangle.center = (eachNote.xPos - p_m.Data.meter, eachNote.yPos)
            newPlot = Plot(eachNote, eachNote.sound, eachNote.image, eachNote.rectangle )
            l_p.Data.objects.append(newPlot)'''

        




'''
class Data():   
    populate_me = True
    current_plot = [] #this is the fundamental unit that will be tracked
    this_section = [] 
    transcript_copy = []
    
    section_local_counter = int(0)
    section_counter_list = []
    current_section = int(0)        
    section_integer = int(0)
    current_sounds = [] 

    notesInternal = []'''

'''for eachNote in currentPlot:
    sounds.append(gni.returnSound(eachNote))'''
    
'''def populateNotes():
    dev notes pay attention to pni.Data.this_section - deprecated reference!!!
    Data.transcript_copy = my.Trn.transcript

    for eachSection in my.Trn.transcript:  #this references a list of lists
            Data.section_local_counter = len(eachSection) # this is an integer counter for my notes in each section of my transcript
            Data.section_counter_list.append(Data.section_local_counter) #this is a list of integer counters 
            #to assist the plotting function so it knows when to stop plotting.
            Data.current_section = Data.section_counter_list[0] #this holds the integer for the plotting function to count
            Data.this_section = Data.transcript_copy[0]
            db.Data.debug_log.append('in pni.populateNotes()')
            
    Data.populateMe = False'''
#this is a list inside of a list - it is the total song
        #print(f' in pni.populate transcript copy {len(I.transcriptCopy)}')
        #print(f' in pni.populate...I.transcriptCopy {I.transcriptCopy}')  #breadcrumb
        #print('why is mySong transcribed incorrectly?')

'''class Plot(): # stands for 'Increment'

    #print('in pni class Inc') #breadcrumb 

    def __init__(self, notesInternal):

        self.notesInternal = notesInternal
        Data.notesInternal = self.notesInternal'''
        
'''def playNotes(self):

        #for eachNote in self.notesInternal:
        for eachNote in Data.notesInternal:
        
            sound = gni.Note.returnSound(eachNote)

            gni.Note.play(sound)

            db.Data.debug_log.append('playing sound in pni.Plot.playNotes()')

def resetPlot(): 
    Data.current_plot = []
    Data.current_sounds = []
    db.Data.debug_log.append('resetPlot() in pni')

def populateSounds():

    for eachNote in Data.current_plot:
        sound = gni.Note.returnSound(eachNote)
        Data.current_sounds.append(sound)
        pb.Data.recording.append(Data.current_sounds)
        db.Data.debug_log.append('append sound in pni.populateSounds()')
        resetPlot()
        
def createPlot(notesExternal):
    
    db.Data.debug_log.append('in pni createPlot')  #breadcrumb
    myPlot = Plot(notesInternal = notesExternal)
    if len(myPlot.notesInternal) > 0: 
        db.Data.debug_log.append('sound plot created')
    else:
        db.Data.debug_log.append('empty plot created in pni.createPlot()')
    Data.current_plot.append(myPlot)
    populateSounds()
    
def resetSection():
    db.Data.debug_log.append('reset Section')
    Data.section_integer = int(0)
    Data.current_section = int(0)
    #section_counter = int(0)
    Data.populate_me = True

def advance():
    try:
        Data.sectionInteger += 1   
        Data.current_section = my.Trn.transcript[Data.sectionInteger]
        db.Data.debug_log.append('advancing section in pni.advance()')
    except:   
        resetSection()
        db.Data.debug_log.append('pni line 72...switch to playback after section advance out of range')
        gatekeeper.Data.current = 'playback' '''
