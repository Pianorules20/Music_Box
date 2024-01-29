#Step1.py

import settings, random, mySong as my, playback, instance as i, generate_notes, gni as gni, debug as db
import populate_settings, gatekeeper, debug as db

def randomShortForm():
    db.Data.debug_log.append('in branches2...random short form')  #breadcrumb
    for eachVoice in i.Data.instruments:
        db.Data.debug_log.append(f'checking length of each voice...{len(eachVoice)}')
    if my.Data.finished == True:
        checkTranscript = []
        for eachSection in my.Data.transcript:
            for eachNote in eachSection:
                Name = gni.Note.returnLetterName(eachNote)
                Octave = gni.Note.returnOctave(eachNote)
                spacer = ' '
                checkTranscript.append(Name)
                checkTranscript.append(Octave)
                checkTranscript.append(spacer)
        db.Data.debug_log.append('in branches2 my.Data.finished = True?')
        db.Data.debug_log.append(f'my.Data.finished = {my.Data.finished}')
        db.Data.debug_log.append('my recording')
        localTrace = print(*checkTranscript, sep = '')
        localTrace = str(localTrace)
        db.Data.debug_log.append(localTrace)
        db.Data.debug_log.append('finished branches2 randomShortForm() Gate = "plot_notes" ')
        gatekeeper.Data.current = 'plot_notes'  #!!!!!!
    
    else:

        for eachVoice in i.Data.instruments:   
            if len(eachVoice) > 0 :  #only runs if the user has a assigned notes to a particular polyphony

                save_place = i.Data.notesRemaining

                while i.Data.notesRemaining > 0 :
                    
                
                    generate_notes.generate()
                    
            
            else:
                    # i was missing my operator parentheses for my p_s.Populate.createRemainingNotes which I have since moved
                i.Data.notesRemaining = save_place
                my.Data.meter  = 0
                #   my.resetSection()
                #i.notesRemaining = settings.Op.notesRemaining # is this correct???
                # i was missing my operator parentheses but i since rewrote this previous line
        
        my.Data.transcript.append(i.Data.current_section) #pay careful attention as this is now a list \
            #inside of a list
            #printer._print_PDF()
    my.Data.finished = True  #are you the culprit that turned my boolean to True too early???
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
            if i.Data.sectionWritten == True: # checks for section Written
                my.Data.generatedStructure.append(newLetter)
                if my.Data.generatedStructure == my.Data.targetStructure:
                    playback.Player.play()
                    #printer._print_PDF()  include a pdf printout of the sheet music
                    my.Data.resetInstance()
                    my.Data.transcriptReset()
                else:
                    my.Data.iReset()
            else:
                if i.notesRemaining >= 0:
                    generate_notes.Generator.generate()
                else:
                    i.sectionWritten = True
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
    print('user constructed')  #breadcrumb 
    for xChar in settings.Preferences.structure:
        if xChar in my.Data.generatedStructure:
            pass
            #mySong.Data.melody = mySong.Data.total
            #mySong.Data.durations = mySong.Data.totalDurations
        else:
            my.Data.generatedStructure.append(xChar)