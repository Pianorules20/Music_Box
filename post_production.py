# post_production.py
import gatekeeper as g, current_section as cs, initializer as init, mySong as my, playback_meter as pm, settings as s
import debug as db

def print_sheet():
    pass
  

def record_audio():
    pass
    # g.Data.current = 'generate notes'


def new_instance():

    if s.Data.structure == 'random short form':
        cs.reset_instance()
        my.reset_transcript()
        pm.reset_meter()
        init.initialize()
        g.Data.current = 'generate notes'
    
    else:
        info = 'add code for new structure'
        print(info)
        db.Data.debug_log.append(info)