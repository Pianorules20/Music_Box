#menu.py
import pygame, display as d, display_interface as di, debug as db, gatekeeper as g, mySong as my
import timer as t, screen_saver as ss, pni #plot_notes_interface

def menu_screen():

    #db.Data.debug_log.append('menu_screen')
    d.Window.frame.fill(ss.Data.rbg,(0,0, di.Data.width, di.Data.height))
    # pygame.draw.rect(d.Window.screen, (100,100,100), (300,800, 100,180), 3,25)

    d.Window.spacebar1 = 'Press Spacebar to Create and Record'
    d.Window.myFont = pygame.font.Font('freesansbold.ttf', 24)
    d.Window.spacebar3 = d.Window.myFont.render(d.Window.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Window.spacebar4 = d.Window.spacebar3.get_rect()
    d.Window.spacebar4.center = (di.Data.width/7, di.Data.height*0.65)
    
    d.Window.escape1 = 'Press Escape to Stop'
    d.Window.escape2 = d.Window.myFont
    d.Window.escape3 = d.Window.escape2.render(d.Window.escape1, True, ss.Data.text, ss.Data.rbg)
    d.Window.escape4 = d.Window.escape3.get_rect()
    d.Window.escape4.center = (di.Data.width/7, di.Data.height*0.6)
    
    d.Window.debug_A = "Press 'D' + 'B' + 'G' to toggle debug screen"
    d.Window.debug_B = d.Window.myFont
    d.Window.debug_C = d.Window.debug_B.render(d.Window.debug_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.debug_D = d.Window.debug_C.get_rect()
    d.Window.debug_D.center = (di.Data.width/7, di.Data.height*0.55)

    credits_A = "Press 'C' + 'R' to toggle credits"
    credits_B = d.Window.myFont
    credits_C  = credits_B.render(credits_A, True, ss.Data.text, ss.Data.rbg)
    credits_D = credits_C.get_rect()
    credits_D.center = (di.Data.width/7, di.Data.height*0.5)

    d.Window.gate_A = 'gate'
    d.Window.gate_B = d.Window.myFont
    d.Window.gate_C = d.Window.gate_B.render(d.Window.gate_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.gate_D = d.Window.gate_C.get_rect()
    d.Window.gate_D.center = (di.Data.width/9.5, di.Data.height*0.4) 
    d.Window.tracer1a = g.Data.current
    d.Window.tracer1b = d.Window.myFont
    d.Window.tracer1c = d.Window.tracer1b.render(d.Window.tracer1a, True, ss.Data.text, ss.Data.rbg)
    d.Window.tracer1d = d.Window.tracer1c.get_rect()
    d.Window.tracer1d.center = (di.Data.width/10, di.Data.height*0.43)

    d.Window.C_S_A = 'current section notes'
    d.Window.C_S_B = d.Window.myFont
    d.Window.C_S_C = d.Window.C_S_B.render(d.Window.C_S_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.C_S_D = d.Window.C_S_C.get_rect()
    d.Window.C_S_D.center = (di.Data.width/9.5, di.Data.height*0.20)
    d.Window.tracer2a = str(f'currentsection = {my.Trn.currentSection}')
    d.Window.tracer2b = d.Window.myFont
    d.Window.tracer2c = d.Window.tracer2b.render(d.Window.tracer2a, True, ss.Data.text, ss.Data.rbg)
    d.Window.tracer2d = d.Window.tracer2c.get_rect()
    d.Window.tracer2d.center = (di.Data.width/10, di.Data.height*0.23)

    d.Window.Trn_A = 'transcript notes' 
    d.Window.Trn_B = d.Window.myFont
    d.Window.Trn_C = d.Window.Trn_B.render(d.Window.Trn_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.Trn_D = d.Window.Trn_C.get_rect()
    d.Window.Trn_D.center = (di.Data.width/9.5, di.Data.height*0.07)
    d.Window.tracer3a = str(f'transcript = {my.Trn.transcript}')
    d.Window.tracer3b = d.Window.myFont
    d.Window.tracer3c = d.Window.tracer3b.render(d.Window.tracer3a, True, ss.Data.text, ss.Data.rbg)
    d.Window.tracer3d = d.Window.tracer3c.get_rect()
    d.Window.tracer3d.center = (di.Data.width/10, di.Data.height*0.1)

    d.Window.Plt_A = 'plotted notes'
    d.Window.Plt_B = d.Window.myFont
    d.Window.Plt_C = d.Window.Plt_B.render(d.Window.Plt_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.Plt_D = d.Window.Plt_C.get_rect()
    d.Window.Plt_D.center = (di.Data.width/9.5, di.Data.height*0.3)
    d.Window.Plt_E = str(pni.Data.current_plot)
    d.Window.Plt_F = d.Window.myFont
    d.Window.Plt_G = d.Window.Plt_F.render(d.Window.Plt_E, True, ss.Data.text, ss.Data.rbg)
    d.Window.Plt_H = d.Window.Plt_G.get_rect()
    d.Window.Plt_H.center = (di.Data.width/10, di.Data.height*0.33)

    '''add a notification for the section counter'''
    d.Window.counter_A = 'section counter'
    d.Window.counter_E = str(pni.Data.section_counter)

    '''blitting'''
    d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)
    d.Window.frame.blit(d.Window.escape3, d.Window.escape4)
    
    d.Window.frame.blit(d.Window.debug_C, d.Window.debug_D)

    d.Window.frame.blit(credits_C, credits_D)
    '''if db.debug_trace == True:    
        d.Window.frame.blit(d.Window.debug_G, d.Window.debug_H)
    else:
        pass'''

    '''d.Window.frame.blit(d.Window.gate_C, d.Window.gate_D)
    d.Window.frame.blit(d.Window.tracer1c, d.Window.tracer1d)'''
    
    '''d.Window.frame.blit(d.Window.C_S_C, d.Window.C_S_D)
    d.Window.frame.blit(d.Window.Trn_C, d.Window.Trn_D)'''

    '''d.Window.frame.blit(d.Window.tracer2c, d.Window.tracer2d)
    d.Window.frame.blit(d.Window.tracer3c, d.Window.tracer3d)'''

    '''d.Window.frame.blit(d.Window.Plt_C, d.Window.Plt_D)
    d.Window.frame.blit(d.Window.Plt_G, d.Window.Plt_H)'''