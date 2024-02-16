#layout_playback_style.py
import state

class Data():

    objects = []

    width = 2000
    height = 1000
    frame_data = (0,0, width, height)
    banner = (width*0.5, height*0.1)
    header = (width*0.5, height*0.2)
    header_2 = (width*0.5, height*0.3)
    footer = (width*0.5, height*0.9)

    x10 = width*0.005
    x20 = width*0.01
    x40 = width*0.03
    x100 = width*0.05
    x200 = width*0.1
    x300 = width*0.15
    x400 = width*0.2
    x500 = width*0.25
    x600 = width*0.3
    x700 = width*0.35
    x800 = width*0.4
    x900 = width*0.45
    x1000 = width*0.5
    x1100 = width*0.55
    x1200 = width*0.6
    x1300 = width*0.65
    x1400 = width*0.70
    x1500 = width*0.75
    x1600 = width*0.8
    x1700 = width*0.85
    x1800 = width*0.9
    x1900 = width*0.95
    x2000 = width

    y50 = height*0.05
    y100 = height*0.1
    y150 = height*0.15
    y200 = height*0.2
    y250 = height*0.25
    y300 = height*0.3
    y350 = height*0.35
    y400 = height*0.4
    y450 = height*0.45
    y500 = height*0.5
    y550 = height*0.55
    y600 = height*0.6
    y650 = height*0.65
    y700 = height*0.7
    y750 = height*0.75
    y800 = height*0.8
    y850 = height*0.85
    y900 = height*0.9
    y950 = height*0.95
    y1000 = height*1

    x_values = [x10, x20, x40, x100, x200, x300, x400, x500, x600, x700, x800, x900, x1000, x1100, x1200, \
              x1300, x1400, x1500, x1600, x1700, x1800, x1900, x2000]

    y_values = [y50, y100, y150, y200, y250, y300, \
                y350, y400, y450, y500, y550, y600, y650, y700, y750, y800, y850, y900, y950, y1000]
    
def populate_objects(note):
    
    if note == 'reset':

        Data.objects = []
        
    else:
        Data.objects.append(note)

 