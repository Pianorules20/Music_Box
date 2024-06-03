#debug_log.py
import screen_saver as ss, display_interface as di, fonts as f, display as d

class Data():
    initialize = 'initialize'

def debug_log_screen():

    '''dev notes create me a pygame surface to blit over the screen'''
    #db.Data.debug_log.append('credits_screen') artifact me it floods the debug log
    d.Data.frame.fill(ss.Data.rbg,(0,0, di.Data.width, di.Data.height))

    #def handle_strings(myText, xAxis, yAxis, leftEdge, rightEdge, bottomEdge, font):

    Data.splash_A = "Press  'S'  to scroll through the log"
    Data.splash_B = f.Data.scripted
    Data.splash_C = Data.splash_B.render(Data.splash_A, True, ss.Data.text, ss.Data.rbg)
    Data.splash_D = Data.splash_C.get_rect()
    Data.splash_D.center = (1000, 50)
    d.Data.frame.blit(Data.splash_C, Data.splash_D)

    #Data.log_A = str(db.Data.debug_log)
    #th.reset_text()
    '''th.handle_strings(Data.log_A, lm.Data.x20-5, lm.Data.y150, lm.Data.x10, lm.Data.x1700, \
                      lm.Data.y1000-30, f.Data.subtitle, auto_scroll = 'yes')'''