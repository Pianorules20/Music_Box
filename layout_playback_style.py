#layout_playback_style.py
import display_interface as di

def initialize():
    di.Data.top_left = (di.Data.width*0.2, di.Data.height*0.2) 
    di.Data.top_middle = (di.Data.width*0.5, di.Data.height*0.2) 
    di.Data.top_right = (di.Data.width*0.8, di.Data.height*0.2) 