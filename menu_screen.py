#menu.py
import pygame, display as d, layout_menu_style as lm, fonts as f, screen_saver as ss 

class Data():
    null = ''

def menu_screen():  
    #d.Data.width = 2000 
    #d.Data.height = 1000 
    #db.Data.debug_log.append('menu_screen')
    d.Window.frame.fill(ss.Data.rbg,(0,0, lm.Data.width, lm.Data.height))
    # pygame.draw.rect(d.Window.screen, (100,100,100), (300,800, 100,180), 3,25)
    d.Window.welcome_A =  'Welcome to the Music Box'
    d.Window.welcome_B = f.Data.large_script
    d.Window.welcome_C = d.Window.welcome_B.render(d.Window.welcome_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.welcome_D = d.Window.welcome_C.get_rect()
    lm.Data.banner_pos = lm.Data.width*0.5-ss.Data.banner_regress
    lm.Data.banner = (lm.Data.banner_pos, lm.Data.height*0.1)
    d.Window.welcome_D.center = lm.Data.banner
    d.Window.frame.blit(d.Window.welcome_C, d.Window.welcome_D)

    d.Window.spacebar1 = 'Press Spacebar to Create and Record'
    d.Window.spacebar2 = f.Data.scripted
    d.Window.spacebar3 = d.Window.spacebar2.render(d.Window.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Window.spacebar4 = d.Window.spacebar3.get_rect()
    d.Window.spacebar4.bottomleft = (lm.Data.x10, lm.Data.y200)
    d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)

    d.Window.escape1 = 'Press Escape to Stop'
    d.Window.escape2 = f.Data.scripted
    d.Window.escape3 = d.Window.escape2.render(d.Window.escape1, True, ss.Data.text, ss.Data.rbg)
    d.Window.escape4 = d.Window.escape3.get_rect()
    d.Window.escape4.bottomleft = (lm.Data.x10, lm.Data.y250)
    d.Window.frame.blit(d.Window.escape3, d.Window.escape4)
    
    d.Window.debug_A = "Press  'D'  +  'B'  +  'G'  to toggle debug screen"
    d.Window.debug_B = f.Data.scripted
    d.Window.debug_C = d.Window.debug_B.render(d.Window.debug_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.debug_D = d.Window.debug_C.get_rect()
    d.Window.debug_D.bottomleft = (lm.Data.x10, lm.Data.y300)
    d.Window.frame.blit(d.Window.debug_C, d.Window.debug_D)
    
    credits_A = "Press  'C'  +  'R'  to toggle credits"
    credits_B = f.Data.scripted
    credits_C  = credits_B.render(credits_A, True, ss.Data.text, ss.Data.rbg)
    credits_D = credits_C.get_rect()
    credits_D.bottomleft = (lm.Data.x10, lm.Data.y350)
    d.Window.frame.blit(credits_C, credits_D)

    quit_A = "Press  'Q'  to Quit"
    quit_B = f.Data.scripted
    quit_C = quit_B.render(quit_A, True, ss.Data.text, ss.Data.rbg)
    quit_D = quit_C.get_rect()
    quit_D.bottomleft = (lm.Data.x10, lm.Data.y400)
    d.Window.frame.blit(quit_C, quit_D)

    if d.Window.quitting == True:
        quit_A = 'Are you sure you want to quit?'
        quit_B = f.Data.large_script
        quit_C = quit_B.render(quit_A, True, ss.Data.text, ss.Data.rbg)
        quit_D = quit_C.get_rect()
        quit_D.center = lm.Data.x1000, lm.Data.y500
        d.Window.frame.blit(quit_C, quit_D)
    else:
        pass

    '''th.reset_text()
    th.handle_strings(Data.null)'''
    # th.handle_strings accepts a string followed by an x-Position then a y-Position     
    