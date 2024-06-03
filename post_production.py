# post_production.py

import gatekeeper as g, current_section as c_s, my_song as my, settings as s, populate_instance as p_i, display_interface as d_i
import playback as pb, debug as db, structure as struc

def print_sheet():
    pass

def record_audio():
    pass
    # g.Data.current = 'generate notes'

def repeat_composition():
    g.Data.current_gate = g.Data.playback
    d_i.Data.current_screen = g.Data.playback
    pb.reset_meter()
    print('in post_production, repeat_composition, resetting playback meter')


def new_instance():

    if s.Data.structure == 'Random Short Form':
        p_i.initialize()
        #c_s.reset_instance()
        my.reset_transcript()
        #pb.reset_meter()
        #struc.reset_data()
        g.Data.current_gate = g.Data.generate_notes
        d_i.Data.current_screen = g.Data.menu

    else:
        info = 'in post_production, new_instance(), add code for new structure'
        print(info)
        info = f'settings.Data.structure = {s.Data.structure}'
        print(info)
        db.Data.debug_log = info
        #db.Data.debug_log.append(info)


def next():
    if s.Data.repeat_composition == True:
        repeat_composition()
    else:
        pass

    if s.Data.new_composition == True:
        new_instance()
    else:
        print('in post_production, neither repeated nor new')
