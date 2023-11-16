#Step1.py

import settings, random, mySong, playback, instance, generate_notes, generate_notes_interface, populate_settings, gatekeeper

def randomShortForm():
    if mySong.Transcription.finished == True:
        myRecording = []
        for eachSection in mySong.Transcription.transcript:
            for eachNote in eachSection:
                Name = generate_notes_interface.Creation.returnLetterName(eachNote)
                Octave = generate_notes_interface.Creation.returnOctave(eachNote)
                spacer = ' '
                myRecording.append(Name)
                myRecording.append(Octave)
                myRecording.append(spacer)
        print(' ')
        print('my recording')
        print(*myRecording, sep = '')
        print(' ')
        gatekeeper.Gate.current = '_plot_notes'
        #mySong.Transcription.transcriptReset
        #mySong.Transcription.instanceReset
        #mySong.Transcription.initializer()

    else:
        for eachVoice in instance.instruments:
            if len(eachVoice) > 0:
                generate_notes.Generator.generate() #this is a while loop and is self-contained
                populate_settings.Populate.createRemainingNotes
                mySong.Transcription.meter  = 0
            
            else:
                pass
        mySong.Transcription.transcript.append(mySong.Transcription.currentSection)
        #printer._print_PDF()
        mySong.Transcription.finished = True
                
def longFormNew():
    if len(mySong.Transcription.generatedStructure) == 0: # this indicates a blank structure 
        mySong.Transcription.createStructure()    # this creates an integer length for the new structure
    else:
        pass
    while mySong.Transcription.newStructureInteger > 0: #this is a counter variable for the new structure
        newLetter = random.choice(['A','B','C','D','E']) #randomizer
        if newLetter in mySong.Transcription.generatedStructure: #checks for duplicate section
            match newLetter: #adds duplicate to final transcript
                case 'A':
                    mySong.Transcription.transcript.append(mySong.Transcription.sectionA)
                case 'B':
                    mySong.Transcription.transcript.append(mySong.Transcription.sectionB)
                case 'C':
                    mySong.Transcription.transcript.append(mySong.Transcription.sectionC)
                case 'D':
                    mySong.Transcription.transcript.append(mySong.Transcription.sectionD)
                case 'E':
                    mySong.Transcription.transcript.append(mySong.Transcription.sectionE)
        else:    
            if instance.sectionWritten == True: # checks for section Written
                mySong.Transcription.generatedStructure.append(newLetter)
                if mySong.Transcription.generatedStructure == mySong.Transcription.targetStructure:
                    playback.Player.play()
                    #printer._print_PDF()  include a pdf printout of the sheet music
                    mySong.Transcription.instanceReset()
                    mySong.Transcription.transcriptReset()
                else:
                    mySong.Transcription.instanceReset()
            else:
                if instance.notesRemaining >= 0:
                    generate_notes.Generator.generate()
                else:
                    instance.sectionWritten = True
                    mySong.Transcription.generatedStructure.append(newLetter)
                    match newLetter:
                        case 'A':
                            for eachNote in mySong.Transcription.currentSection:
                                mySong.Transcription.sectionA.append(mySong.Transcription.currentSection[eachNote])
                        case 'B':
                            for eachNote in mySong.Transcription.currentSection:
                                mySong.Transcription.sectionB.append(mySong.Transcription.currentSection[eachNote])
                        case 'C':
                            for eachNote in mySong.Transcription.currentSection:
                                mySong.Transcription.sectionC.append(mySong.Transcription.currentSection[eachNote])
                        case 'D':
                            for eachNote in mySong.Transcription.currentSection:
                                mySong.Transcription.sectionD.append(mySong.Transcription.currentSection[eachNote])
                        case 'E':
                            for eachNote in mySong.Transcription.currentSection:
                                mySong.Transcription.sectionE.append(mySong.Transcription.currentSection[eachNote])

    '''for x in mySong.Transcription.generatedStructure:
        if x in mySong.Transcription.sectionNames:    
            mySong.Transcription.sectionNames.append(x)
        else:
            pass
        newStructure -= 1'''

def userConstructed():  
    for xChar in settings.Preferences.structure:
        if xChar in mySong.Transcription.generatedStructure:
            pass
            #mySong.Transcription.melody = mySong.Transcription.total
            #mySong.Transcription.durations = mySong.Transcription.totalDurations
        else:
            mySong.Transcription.generatedStructure.append(xChar)
                