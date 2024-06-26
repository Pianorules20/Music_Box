#menu.py
import display as d, layout_menu_style as lm, fonts as f, screen_saver as s_s, debug as db

class Data():
    null = ''

def menu_screen():  
    #d.Data.width = 2000 
    #d.Data.height = 1000 
    #db.Data.debug_log.append('menu_screen')
    d.Data.window.fill(s_s.Data.rbg,(0,0, lm.Data.width, lm.Data.height))
    # pygame.draw.rect(d.Data.screen, (100,100,100), (300,800, 100,180), 3,25)
    d.Data.welcome_A =  'Welcome to the Music Box'
    d.Data.welcome_B = f.Data.large_script
    d.Data.welcome_C = d.Data.welcome_B.render(d.Data.welcome_A, True, s_s.Data.text, s_s.Data.rbg)
    d.Data.welcome_D = d.Data.welcome_C.get_rect()
    lm.Data.banner_pos = lm.Data.width*0.5-s_s.Data.banner_regress
    lm.Data.banner = (lm.Data.banner_pos, lm.Data.height*0.1)
    d.Data.welcome_D.center = lm.Data.banner
    d.Data.window.blit(d.Data.welcome_C, d.Data.welcome_D)

    d.Data.spacebar1 = 'Press Spacebar to Create and Record'
    d.Data.spacebar2 = f.Data.scripted
    d.Data.spacebar3 = d.Data.spacebar2.render(d.Data.spacebar1, True, s_s.Data.text, s_s.Data.rbg)
    d.Data.spacebar4 = d.Data.spacebar3.get_rect()
    d.Data.spacebar4.bottomleft = (lm.Data.x10, lm.Data.y200)
    d.Data.window.blit(d.Data.spacebar3, d.Data.spacebar4)

    d.Data.escape1 = 'Press Escape to Stop'
    d.Data.escape2 = f.Data.scripted
    d.Data.escape3 = d.Data.escape2.render(d.Data.escape1, True, s_s.Data.text, s_s.Data.rbg)
    d.Data.escape4 = d.Data.escape3.get_rect()
    d.Data.escape4.bottomleft = (lm.Data.x10, lm.Data.y250)
    d.Data.window.blit(d.Data.escape3, d.Data.escape4)
    
    d.Data.debug_A = "Press  'D'  +  'B'  +  'G'  to toggle debug screen"
    d.Data.debug_B = f.Data.scripted
    d.Data.debug_C = d.Data.debug_B.render(d.Data.debug_A, True, s_s.Data.text, s_s.Data.rbg)
    d.Data.debug_D = d.Data.debug_C.get_rect()
    d.Data.debug_D.bottomleft = (lm.Data.x10, lm.Data.y300)
    d.Data.window.blit(d.Data.debug_C, d.Data.debug_D)
    
    credits_A = "Press  'C'  +  'R'  to toggle credits"
    credits_B = f.Data.scripted
    credits_C  = credits_B.render(credits_A, True, s_s.Data.text, s_s.Data.rbg)
    credits_D = credits_C.get_rect()
    credits_D.bottomleft = (lm.Data.x10, lm.Data.y350)
    d.Data.window.blit(credits_C, credits_D)

    quit_A = "Press  'Q'  to Quit"
    quit_B = f.Data.scripted
    quit_C = quit_B.render(quit_A, True, s_s.Data.text, s_s.Data.rbg)
    quit_D = quit_C.get_rect()
    quit_D.bottomleft = (lm.Data.x10, lm.Data.y400)
    d.Data.window.blit(quit_C, quit_D)

    if d.Data.quitting == True:
        quit_A = "Press Enter to confirm quit"
        quit_B = f.Data.large_script
        quit_C = quit_B.render(quit_A, True, s_s.Data.text, s_s.Data.rbg)
        quit_D = quit_C.get_rect()
        quit_D.center = lm.Data.x1000, lm.Data.y500
        d.Data.window.blit (quit_C, quit_D)
    else:
        pass

    options_A = "Press  'S'  for  Settings"
    options_B = f.Data.scripted
    options_C = options_B.render(options_A, True, s_s.Data.text, s_s.Data.rbg)
    options_D = options_C.get_rect()
    options_D.bottomleft = (lm.Data.x10, lm.Data.y450)
    d.Data.window.blit(options_C, options_D)

    Data.trace_E = f'debug_log = {db.Data.debug_log}'
    Data.trace_F = f.Data.subtitle
    Data.trace_G = Data.trace_F.render(Data.trace_E, True, s_s.Data.text, s_s.Data.rbg)
    Data.trace_H = Data.trace_G.get_rect()
    Data.trace_H.bottomleft = (lm.Data.x500+10, lm.Data.y500-20)
    d.Data.window.blit(Data.trace_G, Data.trace_H)

    '''th.reset_text()
    th.handle_strings(Data.null)'''
    # th.handle_strings accepts a string followed by an x-Position then a y-Position     
    