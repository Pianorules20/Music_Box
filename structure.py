#Step1.py

import settings, random, mySong as my, playback, current_section as cs, generate_notes as g_n, gni as gni, debug as db
import gatekeeper as g, debug as db

class Data():
    
    save_place = cs.Data.notesRemaining

def flip_save_place():
    Data.save_place = cs.Data.notesRemaining

def randomShortForm():
    #info = 'in_structure...random_short_form'
    #print(info)
    #db.Data.debug_log.append(info)  #breadcrumb
    #for eachVoice in cs.Data.instruments: #debug log 
    #    info = f'checking_length_of_each_voice...{len(eachVoice)}'
    #    print(info)
    #    db.Data.debug_log.append(info)
    if Data.save_place < 1:
        '''checkTranscript = []  #debug log
        for eachSection in my.Data.transcript:
            for eachNote in eachSection:
                Name = gni.Note.returnLetterName(eachNote)
                Octave = gni.Note.returnOctave(eachNote)
                spacer = ' '
                checkTranscript.append(Name)
                checkTranscript.append(Octave)
                checkTranscript.append(spacer)'''
        #info = f'in_structure.py,_checking_mySong.Data.song_finished__{my.Data.song_finished}'
        #print(info)
        #db.Data.debug_log.append(info)
        #db.Data.debug_log.append('in_structure.py,_print_my_recording')
        #localTrace = f"*checkTranscript, sep = '' "
        #print(localTrace)
        #localTrace = print(*checkTranscript, sep = '')
        #localTrace = str(localTrace)
        #db.Data.debug_log.append(localTrace)
        #db.Data.debug_log.append('finished_structure_randomShortForm()_Gate_=_"plot_notes"_')
        g.Data.current_gate = 'plot_notes'  #!!!!!!
    
    else:

        for eachVoice in cs.Data.instruments:   #i need to change this forLoop into a counter possibly needs an interface
            if len(eachVoice) > 0 :  #only runs if the user has a assigned notes to a particular polyphony

                if Data.save_place > 0 :
                    
                    g_n.generate()
                    Data.save_place -= g_n.Data.notes_generated

                else:
                   
                    Data.save_place = cs.Data.notesRemaining #is this correct?
                    cs.transcribe_section() #make certain to add multi-voice functionality to the transcription process.  
                    #should that be in a a transcript interface?
                    my.Data.meter = 0
            else:
                   
                pass

        
        my.Data.transcript.append(cs.Data.current_section) #pay careful attention as this is now a list \
            #inside of a list
            #printer._print_PDF()
    #print(f'in branches2...random short form...checking transcription length {len(my.Data.transcript)}')
    #print(f'my transcript...{my.Data.transcript}')
def longFormNew():
    #print('long form new')   #breadcrumb
    if len(my.Data.generatedStructure) == 0: # this indicates a blank structure 
        my.Data.createStructure()    # this creates an integer length for the new structure
    else:
        pass
    while my.Data.newStructureInteger > 0: #this is a counter variable for the new structure
        newLetter = random.choice(['A','B','C','D','E']) #randomizer
        if newLetter in my.Data.generatedStructure: #checks for duplicate section
            match newLetter: #adds duplicate to final transcript
                case 'A':
                    my.Data.transcript.append(my.Data.sectionA)
                case 'B':
                    my.Data.transcript.append(my.Data.sectionB)
                case 'C':
                    my.Data.transcript.append(my.Data.sectionC)
                case 'D':
                    my.Data.transcript.append(my.Data.sectionD)
                case 'E':
                    my.Data.transcript.append(my.Data.sectionE)
        else:    
            if cs.Data.sectionWritten == True: # checks for section Written
                my.Data.generatedStructure.append(newLetter)
                if my.Data.generatedStructure == my.Data.targetStructure:
                    playback.Data.play()
                    #printer._print_PDF()  include a pdf printout of the sheet music
                    my.Data.resetInstance()
                    my.Data.transcriptReset()
                else:
                    my.Data.iReset()
            else:
                if cs.notesRemaining >= 0:
                    g_n.generate()
                else:
                    cs.Data.sectionWritten = True
                    my.Data.generatedStructure.append(newLetter)
                    match newLetter:
                        case 'A':
                            for eachNote in my.Data.currentSection:
                                my.Data.sectionA.append(my.Data.currentSection[eachNote])
                        case 'B':
                            for eachNote in my.Data.currentSection:
                                my.Data.sectionB.append(my.Data.currentSection[eachNote])
                        case 'C':
                            for eachNote in my.Data.currentSection:
                                my.Data.sectionC.append(my.Data.currentSection[eachNote])
                        case 'D':
                            for eachNote in my.Data.currentSection:
                                my.Data.sectionD.append(my.Data.currentSection[eachNote])
                        case 'E':
                            for eachNote in my.Data.currentSection:
                                my.Data.sectionE.append(my.Data.currentSection[eachNote])

def userConstructed(): 
    print('user_constructed')  #breadcrumb 
    for xChar in settings.Preferences.structure:
        if xChar in my.Data.generatedStructure:
            pass
            #mySong.Data.melody = mySong.Data.total
            #mySong.Data.durations = mySong.Data.totalDurations
        else:
            my.Data.generatedStructure.append(xChar)