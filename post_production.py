# post_production.py
import gatekeeper as g, current_section as c_s, my_song as my, settings as s, populate_settings as p_s
import debug as db, playback as pb

def print_sheet():
    pass

def record_audio():
    pass
    # g.Data.current = 'generate notes'


def new_instance():

    if s.Data.structure == 'random short form':
        c_s.reset_instance()
        my.reset_transcript()
        pb.reset_meter()
        p_s.initialize()
        g.Data.current = 'generate notes'
    
    else:
        info = 'add code for new structure'
        print(info)
        #db.Data.debug_log.append(info)