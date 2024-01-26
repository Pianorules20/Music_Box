# post_production.py
import gatekeeper as g, instance as i, initializer as init, mySong as my, playback_meter as pm

def print_sheet():
    
    i.reset_instance()
    #init.Initializer()
    my.reset_transcript()
    pm.reset_meter()
    g.Data.current = 'generate notes'

def record_audio():
    g.Data.current = 'generate notes'