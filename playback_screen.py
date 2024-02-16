#player.py
import playback as pb, screen_saver as ss, fonts as f, layout_playback_style as l_p, text_handler as th, display as d


#def handle_strings(myText, xAxis, yAxis, leftEdge, rightEdge, bottomEdge, font, multiple):
class Data():
    pass

def playback_screen():

    d.Data.frame.fill(ss.Data.rbg,(0,0, l_p.Data.width, lp.Data.height))

    Data.splash_A = 'My Recording'
    Data.splash_B = f.Data.large_script
    Data.splash_C = Data.splash_B.render(Data.splash_A, True, ss.Data.text, ss.Data.rbg)
    Data.splash_D = Data.splash_C.get_rect()
    Data.splash_D.center = l_p.Data.x1000, l_p.Data.y100
    d.Window.frame.blit(Data.splash_C, Data.splash_D)
    Data.recording_A = pb.Data.recording
    th.reset_text()
    th.handle_strings(Data.recording_A, l_p.Data.x10, l_p.Data.y100, l_p.Data.x10, l_p.Data.x1800, \
                      l_p.Data.y1900, f.Data.large_script, multiple = 'yes')
    for eachNote in l_p.Data.objects:
        d.Data.frame.blit(eachNote.image, rectangle)


'''def menu_screen():  
    #d.Data.width = 2000 
    #d.Data.height = 1000 
    #db.Data.debug_log.append('menu_screen')
    d.Data.frame.fill(ss.Data.rbg,(0,0, lm.Data.width, lm.Data.height))
    # pygame.draw.rect(d.Data.screen, (100,100,100), (300,800, 100,180), 3,25)
    d.Data.welcome_A =  'Welcome to the Music Box'
    d.Data.welcome_B = f.Data.large_script
    d.Data.welcome_C = d.Data.welcome_B.render(d.Data.welcome_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.welcome_D = d.Data.welcome_C.get_rect()
    lm.Data.banner_pos = lm.Data.width*0.5-ss.Data.banner_regress
    lm.Data.banner = (lm.Data.banner_pos, lm.Data.height*0.1)
    d.Data.welcome_D.center = lm.Data.banner
    d.Data.frame.blit(d.Data.welcome_C, d.Data.welcome_D)

    d.Data.spacebar1 = 'Press Spacebar to Create and Record'
    d.Data.spacebar2 = f.Data.scripted
    d.Data.spacebar3 = d.Data.spacebar2.render(d.Data.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Data.spacebar4 = d.Data.spacebar3.get_rect()
    d.Data.spacebar4.bottomleft = (lm.Data.x10, lm.Data.y200)
    d.Data.frame.blit(d.Data.spacebar3, d.Data.spacebar4)

    d.Data.escape1 = 'Press Escape to Stop'
    d.Data.escape2 = f.Data.scripted
    d.Data.escape3 = d.Data.escape2.render(d.Data.escape1, True, ss.Data.text, ss.Data.rbg)
    d.Data.escape4 = d.Data.escape3.get_rect()
    d.Data.escape4.bottomleft = (lm.Data.x10, lm.Data.y250)
    d.Data.frame.blit(d.Data.escape3, d.Data.escape4)
    
    d.Data.debug_A = "Press  'D'  +  'B'  +  'G'  to toggle debug screen"
    d.Data.debug_B = f.Data.scripted
    d.Data.debug_C = d.Data.debug_B.render(d.Data.debug_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.debug_D = d.Data.debug_C.get_rect()
    d.Data.debug_D.bottomleft = (lm.Data.x10, lm.Data.y300)
    d.Data.frame.blit(d.Data.debug_C, d.Data.debug_D)
    
    credits_A = "Press  'C'  +  'R'  to toggle credits"
    credits_B = f.Data.scripted
    credits_C  = credits_B.render(credits_A, True, ss.Data.text, ss.Data.rbg)
    credits_D = credits_C.get_rect()
    credits_D.bottomleft = (lm.Data.x10, lm.Data.y350)
    d.Data.frame.blit(credits_C, credits_D)

    quit_A = "Press  'Q'  to Quit"
    quit_B = f.Data.scripted
    quit_C = quit_B.render(quit_A, True, ss.Data.text, ss.Data.rbg)
    quit_D = quit_C.get_rect()
    quit_D.bottomleft = (lm.Data.x10, lm.Data.y400)
    d.Data.frame.blit(quit_C, quit_D)

    if d.Data.quitting == True:
        quit_A = "Press Enter to confirm quit"
        quit_B = f.Data.large_script
        quit_C = quit_B.render(quit_A, True, ss.Data.text, ss.Data.rbg)
        quit_D = quit_C.get_rect()
        quit_D.center = lm.Data.x1000, lm.Data.y500
        d.Data.frame.blit (quit_C, quit_D)
    else:
        pass

    options_A = "Press  'O'  for Options"
    options_B = f.Data.scripted
    options_C = options_B.render(options_A, True, ss.Data.text, ss.Data.rbg)
    options_D = options_C.get_rect()
    options_D.bottomleft = (lm.Data.x10, lm.Data.y450)
    d.Data.frame.blit(options_C, options_D)'''
'''th.reset_text()
    th.handle_strings(Data.null)'''
    # th.handle_strings accepts a string followed by an x-Position then a y-Position     
    