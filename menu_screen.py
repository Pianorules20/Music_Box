#menu.py
import pygame, display as d, display_interface as di, debug as db, gatekeeper as g, mySong as my
import timer as t, fonts as f, screen_saver as ss, text_handler as th, pni #plot_notes_interface

def menu_screen():  

    #db.Data.debug_log.append('menu_screen')
    d.Window.frame.fill(ss.Data.rbg,(0,0, di.Data.width, di.Data.height))
    # pygame.draw.rect(d.Window.screen, (100,100,100), (300,800, 100,180), 3,25)
    d.Window.welcome_A =  'Welcome to the Music Box'
    d.Window.welcome_B = f.Data.large_script
    d.Window.welcome_C = d.Window.welcome_B.render(d.Window.welcome_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.welcome_D = d.Window.welcome_C.get_rect()
    di.Data.banner_pos = di.Data.width*0.5-ss.Data.banner_regress
    di.Data.banner = (di.Data.banner_pos, di.Data.height*0.1)
    d.Window.welcome_D.center = di.Data.banner
    d.Window.frame.blit(d.Window.welcome_C, d.Window.welcome_D)

    d.Window.spacebar1 = 'Press Spacebar to Create and Record'
    d.Window.spacebar2 = f.Data.scripted
    d.Window.spacebar3 = d.Window.spacebar2.render(d.Window.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Window.spacebar4 = d.Window.spacebar3.get_rect()
    d.Window.spacebar4.bottomleft = di.Data.left_col_2
    d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)

    d.Window.escape1 = 'Press Escape to Stop'
    d.Window.escape2 = f.Data.scripted
    d.Window.escape3 = d.Window.escape2.render(d.Window.escape1, True, ss.Data.text, ss.Data.rbg)
    d.Window.escape4 = d.Window.escape3.get_rect()
    d.Window.escape4.bottomleft = di.Data.left_col_4
    d.Window.frame.blit(d.Window.escape3, d.Window.escape4)
    
    d.Window.debug_A = "Press 'D' + 'B' + 'G' to toggle debug screen"
    d.Window.debug_B = f.Data.scripted
    d.Window.debug_C = d.Window.debug_B.render(d.Window.debug_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.debug_D = d.Window.debug_C.get_rect()
    d.Window.debug_D.bottomleft = di.Data.left_col_6
    d.Window.frame.blit(d.Window.debug_C, d.Window.debug_D)
    
    credits_A = "Press 'C' + 'R' to toggle credits"
    credits_B = f.Data.scripted
    credits_C  = credits_B.render(credits_A, True, ss.Data.text, ss.Data.rbg)
    credits_D = credits_C.get_rect()
    credits_D.bottomleft = di.Data.left_col_8
    d.Window.frame.blit(credits_C, credits_D)

    th.reset_text()
    th.handle_strings('hello B, testing my parameters with a long sentence designed to bleed over into the next line??? \
                   how much is it going to take to get this sentence on the ground floor?', 20, 650, 20, 900, 900, f.Data.scripted) 
    # th.handle_strings accepts a string followed by an x-Position then a y-Position     

    '''add a notification for the section counter'''
    d.Window.sec_counter_A = 'section counter'
    d.Window.counter_E = str(pni.Data.section_counter)