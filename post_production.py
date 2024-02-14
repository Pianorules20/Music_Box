# post_production.py
import gatekeeper as g, current_section as c_s, my_song as my, playback_meter as p_m, settings as s, populate_settings as p_s
import debug as db

def print_sheet():
    pass
  

def record_audio():
    pass
    # g.Data.current = 'generate notes'


def new_instance():

    if s.Data.structure == 'random short form':
        c_s.reset_instance()
        my.reset_transcript()
        p_m.reset_meter()
        p_s.initialize()
        g.Data.current = 'generate notes'
    
    else:
        info = 'add code for new structure'
        print(info)
        db.Data.debug_log.append(info)