#Step1.py

import settings, random, mySong as m_s, playback, current_section as c_s, generate_notes as g_n, gni as gni, debug as db
import gatekeeper as g, debug as db

class Data():
    
    save_place = c_s.Data.notesRemaining
    voice_counter = int(0)
    song_finished = False

def flip_save_place():
    Data.save_place = c_s.Data.notesRemaining

'''def advance_voice():
    try:
        Data.voice_counter += 1
    except Exception as e:
        print(e)
        db.Data.debug_log.append(e)'''

def advance_data():
    
    try:

        Data.voice_counter = int(0)
    
    except:

        info = 'last_voice_finished'
        
        print(info)
        
        db.Data.debug_log.append(info)

        song_finished = not song_finished

        Data.save_place = c_s.Data.notesRemaining


def randomShortForm():
    #info = 'in_structure...random_short_form'
    #print(info)
    #db.Data.debug_log.append(info)  #breadcrumb
    #for eachVoice in cs.Data.instruments: #debug log 
    #    info = f'checking_length_of_each_voice...{len(eachVoice)}'
    #    print(info)
    #    db.Data.debug_log.append(info)
    
    
    
    if Data.song_finished == True:
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

        #for eachVoice in cs.Data.instruments:   #i need to change this forLoop into a counter possibly needs an interface

        current_voice = c_s.Data.voices_list[Data.voice_counter]
        if len(current_voice) > 0:

            if Data.save_place > 0 :
                
                g_n.generate(current_voice)
                
                Data.save_place -= g_n.Data.notes_generated

            else:
                
                c_s.transcribe_voice() 
                
                m_s.Data.meter = 0
        
        else:
                
            pass
    
        advance_data()

        
        m_s.Data.transcript.append(c_s.Data.current_section) #pay careful attention as this is now a list \
            #inside of a list
            #printer._print_PDF()
    #print(f'in branches2...random short form...checking transcription length {len(my.Data.transcript)}')
    #print(f'my transcript...{my.Data.transcript}')
def longFormNew():
    #print('long form new')   #breadcrumb
    if len(m_s.Data.generatedStructure) == 0: # this indicates a blank structure 
        m_s.Data.createStructure()    # this creates an integer length for the new structure
    else:
        pass
    while m_s.Data.newStructureInteger > 0: #this is a counter variable for the new structure
        newLetter = random.choice(['A','B','C','D','E']) #randomizer
        if newLetter in m_s.Data.generatedStructure: #checks for duplicate section
            match newLetter: #adds duplicate to final transcript
                case 'A':
                    m_s.Data.transcript.append(m_s.Data.sectionA)
                case 'B':
                    m_s.Data.transcript.append(m_s.Data.sectionB)
                case 'C':
                    m_s.Data.transcript.append(m_s.Data.sectionC)
                case 'D':
                    m_s.Data.transcript.append(m_s.Data.sectionD)
                case 'E':
                    m_s.Data.transcript.append(m_s.Data.sectionE)
        else:    
            if c_s.Data.sectionWritten == True: # checks for section Written
                m_s.Data.generatedStructure.append(newLetter)
                if m_s.Data.generatedStructure == m_s.Data.targetStructure:
                    playback.Data.play()
                    #printer._print_PDF()  include a pdf printout of the sheet music
                    m_s.Data.resetInstance()
                    m_s.Data.transcriptReset()
                else:
                    m_s.Data.iReset()
            else:
                if c_s.notesRemaining >= 0:
                    g_n.generate()
                else:
                    c_s.Data.sectionWritten = True
                    m_s.Data.generatedStructure.append(newLetter)
                    match newLetter:
                        case 'A':
                            for eachNote in m_s.Data.currentSection:
                                m_s.Data.sectionA.append(m_s.Data.currentSection[eachNote])
                        case 'B':
                            for eachNote in m_s.Data.currentSection:
                                m_s.Data.sectionB.append(m_s.Data.currentSection[eachNote])
                        case 'C':
                            for eachNote in m_s.Data.currentSection:
                                m_s.Data.sectionC.append(m_s.Data.currentSection[eachNote])
                        case 'D':
                            for eachNote in m_s.Data.currentSection:
                                m_s.Data.sectionD.append(m_s.Data.currentSection[eachNote])
                        case 'E':
                            for eachNote in m_s.Data.currentSection:
                                m_s.Data.sectionE.append(m_s.Data.currentSection[eachNote])

def userConstructed(): 
    print('user_constructed')  #breadcrumb 
    for xChar in settings.Preferences.structure:
        if xChar in m_s.Data.generatedStructure:
            pass
            #mySong.Data.melody = mySong.Data.total
            #mySong.Data.durations = mySong.Data.totalDurations
        else:
            m_s.Data.generatedStructure.append(xChar)