#Step1.py

import settings, random, mySong as my, playback, instance, generate_notes, generate_notes_interface as gni 
import populate_settings, gatekeeper

def randomShortForm():
    print('random short form')  #breadcrumb
    if my.Trn.finished == True:
        checkTranscript = []
        for eachSection in my.Trn.transcript:
            for eachNote in eachSection:
                Name = gni.Note.returnLetterName(eachNote)
                Octave = gni.Note.returnOctave(eachNote)
                spacer = ' '
                checkTranscript.append(Name)
                checkTranscript.append(Octave)
                checkTranscript.append(spacer)
        print(' ')
        print('my recording')
        print(*checkTranscript, sep = '')
        print(' ')
        gatekeeper.Gate.current = 'plot_notes'
        '''The following three lines likely need to be deleted as they no longer fit with my 
        'gatekeeper' paradigm
        #mySong.Trn.transcriptReset
        #mySong.Trn.instanceReset
        #mySong.Trn.initializer()'''

    else:
        for eachVoice in instance.instruments:
            if len(eachVoice) > 0:
                generate_notes.Generator.generate() #this is a while loop and is self-contained
                populate_settings.Populate.createRemainingNotes
                my.Trn.meter  = 0
            
            else:
                pass
        my.Trn.transcript.append(my.Trn.currentSection) #pay careful attention as this is now a list \
        #inside of a list
        #printer._print_PDF()
        my.Trn.finished = True
                
def longFormNew():
    print('long form new')   #breadcrumb
    if len(my.Trn.generatedStructure) == 0: # this indicates a blank structure 
        my.Trn.createStructure()    # this creates an integer length for the new structure
    else:
        pass
    while my.Trn.newStructureInteger > 0: #this is a counter variable for the new structure
        newLetter = random.choice(['A','B','C','D','E']) #randomizer
        if newLetter in my.Trn.generatedStructure: #checks for duplicate section
            match newLetter: #adds duplicate to final transcript
                case 'A':
                    my.Trn.transcript.append(my.Trn.sectionA)
                case 'B':
                    my.Trn.transcript.append(my.Trn.sectionB)
                case 'C':
                    my.Trn.transcript.append(my.Trn.sectionC)
                case 'D':
                    my.Trn.transcript.append(my.Trn.sectionD)
                case 'E':
                    my.Trn.transcript.append(my.Trn.sectionE)
        else:    
            if instance.sectionWritten == True: # checks for section Written
                my.Trn.generatedStructure.append(newLetter)
                if my.Trn.generatedStructure == my.Trn.targetStructure:
                    playback.Player.play()
                    #printer._print_PDF()  include a pdf printout of the sheet music
                    my.Trn.instanceReset()
                    my.Trn.transcriptReset()
                else:
                    my.Trn.instanceReset()
            else:
                if instance.notesRemaining >= 0:
                    generate_notes.Generator.generate()
                else:
                    instance.sectionWritten = True
                    my.Trn.generatedStructure.append(newLetter)
                    match newLetter:
                        case 'A':
                            for eachNote in my.Trn.currentSection:
                                my.Trn.sectionA.append(my.Trn.currentSection[eachNote])
                        case 'B':
                            for eachNote in my.Trn.currentSection:
                                my.Trn.sectionB.append(my.Trn.currentSection[eachNote])
                        case 'C':
                            for eachNote in my.Trn.currentSection:
                                my.Trn.sectionC.append(my.Trn.currentSection[eachNote])
                        case 'D':
                            for eachNote in my.Trn.currentSection:
                                my.Trn.sectionD.append(my.Trn.currentSection[eachNote])
                        case 'E':
                            for eachNote in my.Trn.currentSection:
                                my.Trn.sectionE.append(my.Trn.currentSection[eachNote])

    '''for x in mySong.Trn.generatedStructure:
        if x in mySong.Trn.sectionNames:    
            mySong.Trn.sectionNames.append(x)
        else:
            pass
        newStructure -= 1'''

def userConstructed(): 
    print('user constructed')  #breadcrumb 
    for xChar in settings.Preferences.structure:
        if xChar in my.Trn.generatedStructure:
            pass
            #mySong.Trn.melody = mySong.Trn.total
            #mySong.Trn.durations = mySong.Trn.totalDurations
        else:
            my.Trn.generatedStructure.append(xChar)
                