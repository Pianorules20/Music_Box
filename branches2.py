#Step1.py

import settings, random, mySong as my, playback, instance, generate_notes, gni as gni 
import populate_settings, gatekeeper, debug as db

def randomShortForm():
    print('in branches2...random short form')  #breadcrumb
    for eachVoice in instance.instruments:
        print(f'checking length of each voice...{len(eachVoice)}')
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
        print('in branches2 my.Trn.finished = True?')
        print(f'my.Trn.finished = {my.Trn.finished}')
        print('my recording')
        localTrace = print(*checkTranscript, sep = '')
        localTrace = str(localTrace)
        db.tracer3 = localTrace
        print(' ')
        gatekeeper.Gate.current = 'plot_notes'
    
    else:

        for eachVoice in instance.instruments:   
            if len(eachVoice) > 0 :  #only runs if the user has a assigned notes to a particular polyphony

                save_place = instance.notesRemaining

                while instance.notesRemaining > 0 :
                    
                
                    generate_notes.generate()
                    
            
            else:
                # i was missing my operator parentheses for my p_s.Populate.createRemainingNotes which I have since moved
                instance.notesRemaining = save_place
                my.Trn.meter  = 0
                #   my.resetSection()
                #instance.notesRemaining = settings.Op.notesRemaining # is this correct???
                # i was missing my operator parentheses but i since rewrote this previous line
        
        my.Trn.transcript.append(my.Trn.currentSection) #pay careful attention as this is now a list \
            #inside of a list
            #printer._print_PDF()
    my.Trn.finished = True  #are you the culprit that turned my boolean to True too early???
    #print(f'in branches2...random short form...checking transcription length {len(my.Trn.transcript)}')
    #print(f'my transcript...{my.Trn.transcript}')
def longFormNew():
    #print('long form new')   #breadcrumb
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

def userConstructed(): 
    print('user constructed')  #breadcrumb 
    for xChar in settings.Preferences.structure:
        if xChar in my.Trn.generatedStructure:
            pass
            #mySong.Trn.melody = mySong.Trn.total
            #mySong.Trn.durations = mySong.Trn.totalDurations
        else:
            my.Trn.generatedStructure.append(xChar)
                
