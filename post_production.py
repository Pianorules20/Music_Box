# post_production.py
import gatekeeper as g, current_section as cs, initializer as init, mySong as my, playback_meter as pm

def print_sheet():
    pass
  

def record_audio():
    pass
    # g.Data.current = 'generate notes'


def new_instance():

    cs.reset_instance()
    my.reset_transcript()
    pm.reset_meter()
    init.initialize()
    g.Data.current = 'generate notes'