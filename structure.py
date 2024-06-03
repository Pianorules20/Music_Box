#structure.py

import settings, random, my_song as m_s, playback, current_section as c_s, generate_notes as g_n, gni as gni
import gatekeeper as g

class Data():
    
    save_place = c_s.Data.notesRemaining
    voice_counter = int(0)
    length_counter = len(c_s.Data.voices_list)
    current_voice = c_s.Data.voices_list[voice_counter]

def reset_data():
    print('in structure, reset_data()')
    #Data.save_place = c_s.Data.notesRemaining
    Data.voice_counter = int(0)
    Data.length_counter = len(c_s.Data.voices_list)
    Data.current_voice = c_s.Data.voices_list[Data.voice_counter]  # watch out it may need to be refreshed

def reset_save_place():
    Data.save_place = c_s.Data.notesRemaining

def advance_voice_short_form():

    Data.voice_counter += 1
    info = f'voice_counter_{Data.voice_counter}'        
    print(info)
    #db.Data.debug_log.append(info)
    info = f'length_counter_{Data.length_counter}'
    print(info)
    #db.Data.debug_log.append(info)
    try:
        Data.current_voice = c_s.Data.voices_list[Data.voice_counter]
        Data.save_place = c_s.Data.notesRemaining
        info = 'finished_current_voice'
        print(info)
        #db.Data.debug_log.append(info)

    except:
        #Data.voice_counter = int(0)
        #Data.song_finished = not Data.song_finished                        #BREADCRUMB
        info = 'finished_last_voice in structure.py'
        print(info)
        #db.Data.debug_log.append(info)

        c_s.Data.sectionWritten = not c_s.Data.sectionWritten
        info = 'sectionWritten in structure.py'
        print(info)
        #db.Data.debug_log.append(info)

        Data.save_place = c_s.Data.notesRemaining
        info = 'save_place reset in structure.py'
        print(info)
        #db.Data.debug_log.append(info)

        m_s.Data.song_finished = not m_s.Data.song_finished
        m_s.append_section()
        g.Data.current_gate = g.Data.plot_notes
        print('entering plot_notes')
        reset_data()

def randomShortForm():
    info = 'in_structure...random_short_form'
    print(info)
    #db.Data.debug_log.append(info)  #breadcrumb
    #for eachVoice in cs.Data.instruments: #debug log 
    #    info = f'checking_length_of_each_voice...{len(eachVoice)}'
    #    print(info)
    #    db.Data.debug_log.append(info)
    
    
    
    if m_s.Data.song_finished == True:

        g.Data.current_gate = g.Data.plot_notes  #!!!!!!
    
    else:
    
        if len(Data.current_voice) > 0:

            if Data.save_place > 0 :
                
                g_n.generate(Data.current_voice)
                
                Data.save_place -= g_n.Data.notes_generated

                info = f'Data.save_place = {Data.save_place}'
                print(info)
                #db.Data.debug_log.append(info)


            else:
                
                c_s.transcribe_voice() 
                
                m_s.Data.meter = 0

                advance_voice_short_form()


        
        else:

            info = 'skipping empty voice'
            print(info)
            #db.Data.debug_log.append(info)
            
            advance_voice_short_form()


            '''the line below i think was an inadvertent duplicate of the c_s.transcribe_voice()  was this causing problems???'''
        #m_s.Data.transcript.append(c_s.Data.current_section) #pay careful attention as this is now a list \
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