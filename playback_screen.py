#player.py
import playback as pb, screen_saver as ss, fonts as f, layout_playback_style as lp, text_handler as th
import display as d
#def handle_strings(myText, xAxis, yAxis, leftEdge, rightEdge, bottomEdge, font, multiple):
class Data():
    pass

def playback_screen():
    
    Data.splash_A = 'My Recording'
    Data.splash_B = f.Data.large_script
    Data.splash_C = Data.splash_B.render(Data.splash_A, True, ss.Data.text, ss.Data.rbg)
    Data.splash_D = Data.splash_C.get_rect()
    Data.splash_D.center = lp.Data.x1000, lp.Data.y100
    d.Window.frame.blit(Data.splash_C, Data.splash_D)
    Data.recording_A = pb.Data.recording
    th.reset_text()
    th.handle_strings(Data.recording_A, lp.Data.x10, lp.Data.y100, lp.Data.x10, lp.Data.x1800, \
                      lp.Data.y1900, f.Data.large_script, multiple = 'yes')

