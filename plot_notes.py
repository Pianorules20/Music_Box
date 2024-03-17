#plot_notes.py
import my_song as m_s, playback as pb, display_interface as d_i, settings as s
import debug as db, gatekeeper as g, pni #plot_notes_interfaces

class Data():
    #generic / pass once
    timer = s.Data.metronome
    populate_copy = True
    plot_copy = []
    num_sections = len(plot_copy)
    total_length = int(0)
    completion_float_count = float(0)
    finished_plotting = False
    #section_related 
    populate__this_section = True
    this_section_copy = []
    section_counter = int(0)
    #each pass
    this_section_plot_counter = int(0)
    section_meter = int(0)
    song_meter = int(0)

def advance_meter():
    Data.section_meter += Data.timer
    Data.song_meter += Data.timer

def reset_data():
    print('resetting Data in plot_notes')
    #generic / pass once
    Data.timer = s.Data.metronome
    Data.populate_copy = True
    Data.plot_copy = []
    Data.num_sections = len(Data.plot_copy)
    Data.total_length = int(0)
    Data.completion_float_count = float(0)
    #section_related
    Data.populate__this_section = True  
    Data.this_section_copy = []
    #Data.section_counter = int(0)
    Data.section_meter = int(0)
    #each pass
    Data.this_section_plot_counter = int(0)
    
    if Data.finished_plotting == True:
        print('finished plotting')
        Data.populate_copy = True
        pb.Data.plot_meter_saved = int(Data.song_meter)
        Data.song_meter = int(0)
        Data.finished_plotting = False
        g.Data.current_gate = 'playback'
        d_i.Data.current_screen =  'playback'
    else:
        pass
                    
def advance_section_counter():
    print('advancing section counter')
    try:
        #Data.section_counter += int(1)
        if Data.num_sections == 0:
            print('end of sections in plot_notes.py')
            Data.finished_plotting = True
            reset_data()
        else:
            Data.section_counter += int(1)
            print(f'in advance_section_counter section counter {Data.section_counter}')
        reset_data()
        print(f'in p_n advance_section_counter()...Data.section_counter = {Data.section_counter}')
    except:
        print('end of sections in plot_notes.py')
        Data.finished_plotting = True
        reset_data()

def plot_notes():
    #careful Bryan!!! Make certain that you reset your meter if necessary and or get your sections correci
    #info = f'transcript_{m_s.Data.transcript}'
    #print(info)    i
    #db.Data.debug_log.append(info)
    
    Data.timer = s.Data.metronome
    if Data.populate_copy == True:
        Data.populate_copy = not Data.populate_copy
        Data.plot_copy = m_s.Data.transcript   
        Data.num_sections = len(Data.plot_copy) 
        for eachSection in Data.plot_copy:
            for eachNote in eachSection:
                Data.total_length += int(1)
    else:
        pass

    if Data.populate__this_section == True:
        Data.populate__this_section = not Data.populate__this_section
        Data.this_section_copy = Data.plot_copy[Data.section_counter]
        Data.this_section_plot_counter = len(Data.this_section_copy)
    else:
        pass
        
    if Data.this_section_plot_counter > 0:
        
        #info = f'p_n_len_final_copy_this_section_{pb.Data.plot_copy[Data.section_counter]}'
        #print(info)
        #db.Data.debug_log.append(info)
        
        for eachNote in Data.this_section_copy:
            if Data.section_meter >= eachNote.xPos:
                pni.Data.current_plot.append(eachNote)
                Data.this_section_copy.remove(eachNote)  
                Data.total_length -= int(1)
                Data.this_section_plot_counter -= int(1)

            else: 
                pass
                
                    
        pni.create_plot()
        pni.Data.current_plot = [] #!!!
        advance_meter()

    else:
        #info = f'p_n_current_section_empty_{Data.section_counter}'
        advance_section_counter()
    Data.completion_float_count = float(Data.total_length/100)
    info = f'in plot_notes, completion_float_count {Data.completion_float_count}'
    print(info)
    db.Data.debug_log = info
    info = f'this_section_plot_counter {Data.this_section_plot_counter}'
    print(info)
    db.Data.debug_log = info
    print(f'num_sections {Data.num_sections}')