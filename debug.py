#debug.py
import pygame, display as d, mySong as my, gatekeeper as g, pni #plot_notes_interface
import screen_saver as ss, text_handler as th, display_interface as di, fonts as f

class Data():
    debug_trace = False
    debug_log = ['begin program']
    fonts_gate = True

def reset():
    Data.debug_log = ['begin program']
def print_log():
    print(Data.debug_log)

def debug_screen():
    #Data.debug_log.append('debug_screen')
    d.Window.frame.fill(ss.Data.rbg, di.Data.frame_data)
    # pygame.draw.rect(d.Window.screen, (100,100,100), (300,800, 100,180), 3,25)

    ''' artifact for aqcuiring system available fonts
        !!! important note !!! the devs seem to have 'hidden' some of the more proprietary fonts with
        an 'noto' prefix to some of the fonts.  This prefix must be removed for them to function although 
        they do not actually function as the fonts themselves rather as a smaller normal font
    Data.myFonts = pygame.font.get_fonts()
    Data.myFontsA = str(Data.myFonts)
    Data.myFontsB = pygame.font.Font('freesansbold.ttf', 24)
    Data.myFontsC = Data.myFontsB.render(Data.myFontsA, True, ss.Data.text, ss.Data.rbg)
    Data.myFontsD = Data.myFontsC.get_rect()
    Data.myFontsD.center = (di.Data.width*.5, di.Data.height*0.9)
    d.Window.frame.blit(Data.myFontsC, Data.myFontsD)
    if Data.fonts_gate == True:
        print(Data.myFontsA)
        Data.fonts_gate = False
    else:
        pass'''

    d.Window.splash_A = 'DEBUG SCREEN'
    d.Window.splash_B = f.Data.title
    d.Window.splash_C = d.Window.splash_B.render(d.Window.splash_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.splash_D = d.Window.splash_C.get_rect()
    d.Window.splash_D.center = di.Data.header
    d.Window.frame.blit(d.Window.splash_C, d.Window.splash_D)

    d.Window.spacebar1 = 'Press Spacebar to Create and Record'
    d.Window.spacebar2 = f.Data.scripted
    d.Window.spacebar3 = d.Window.spacebar2.render(d.Window.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Window.spacebar4 = d.Window.spacebar3.get_rect()
    d.Window.spacebar4.bottomleft = (10, 50)
    d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)
         
    d.Window.escape1 = 'Press Escape to Stop'
    d.Window.escape2 = f.Data.scripted
    d.Window.escape3 = d.Window.escape2.render(d.Window.escape1, True, ss.Data.text, ss.Data.rbg)
    d.Window.escape4 = d.Window.escape3.get_rect()
    d.Window.escape4.bottomleft = (10, 100)
    d.Window.frame.blit(d.Window.escape3, d.Window.escape4)

    Data.trace_A = 'Press T for debug trace'
    Data.trace_B = f.Data.scripted
    Data.trace_C = Data.trace_B.render(Data.trace_A, True, ss.Data.text, ss.Data.rbg)
    Data.trace_D = Data.trace_C.get_rect()
    Data.trace_D.bottomleft = (10, 200)
    Data.trace_E = Data.debug_log[-1]
    Data.trace_F = f.Data.subtitle
    Data.trace_G = Data.trace_F.render(Data.trace_E, True, ss.Data.text, ss.Data.rbg)
    Data.trace_H = Data.trace_G.get_rect()
    Data.trace_H.bottomleft = (50, 225)
    d.Window.frame.blit(Data.trace_C, Data.trace_D)
    if Data.debug_trace == True:    
        d.Window.frame.blit(Data.trace_G, Data.trace_H)
    else:
        pass

    Data.log_A = "Press 'L' + 'G'for Debug Log"
    Data.log_B = f.Data.scripted
    Data.log_C = Data.log_B.render(Data.log_A, True, ss.Data.text, ss.Data.rbg)
    Data.log_D = Data.log_C.get_rect()
    Data.log_D.bottomleft = (10, 150)
    d.Window.frame.blit(Data.log_C, Data.log_D)

    d.Window.gate_A = 'Gate'
    d.Window.gate_B = f.Data.scripted
    d.Window.gate_C = d.Window.gate_B.render(d.Window.gate_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.gate_D = d.Window.gate_C.get_rect()
    d.Window.gate_D.bottomleft = (10, 310)
    d.Window.tracer1a = g.Data.current
    d.Window.tracer1b = f.Data.subtitle
    d.Window.tracer1c = d.Window.tracer1b.render(d.Window.tracer1a, True, ss.Data.text, ss.Data.rbg)
    d.Window.tracer1d = d.Window.tracer1c.get_rect()
    d.Window.tracer1d.bottomleft = (50, 350)
    d.Window.frame.blit(d.Window.gate_C, d.Window.gate_D)
    d.Window.frame.blit(d.Window.tracer1c, d.Window.tracer1d)

    d.Window.C_S_A = 'current section notes'
    d.Window.C_S_B = f.Data.scripted
    d.Window.C_S_C = d.Window.C_S_B.render(d.Window.C_S_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.C_S_D = d.Window.C_S_C.get_rect()
    d.Window.C_S_D.bottomleft = (1000, 400)
    d.Window.tracer2a = str(f'currentsection = {my.Trn.currentSection}')
    d.Window.tracer2b = f.Data.subtitle
    d.Window.tracer2c = d.Window.tracer2b.render(d.Window.tracer2a, True, ss.Data.text, ss.Data.rbg)
    #d.Window.tracer2d = d.Window.tracer2c.get_rect()
    d.Window.frame.blit(d.Window.C_S_C, d.Window.C_S_D)
    th.reset_text()
    th.handle_strings(d.Window.tracer2a, 1000, 450, 1000, 1990, 900, f.Data.subtitle, multiple = 'yes')

    d.Window.Plt_A = 'plotted notes'
    d.Window.Plt_B = f.Data.scripted
    d.Window.Plt_C = d.Window.Plt_B.render(d.Window.Plt_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.Plt_D = d.Window.Plt_C.get_rect()
    d.Window.Plt_D.bottomleft = (10, 550)
    d.Window.Plt_E = str(f'pni this section {pni.Data.current_plot}')
    d.Window.Plt_F = f.Data.subtitle
    d.Window.Plt_G = d.Window.Plt_F.render(d.Window.Plt_E, True, ss.Data.text, ss.Data.rbg)
    d.Window.Plt_H = d.Window.Plt_G.get_rect()
    d.Window.Plt_H.bottomleft = (40, 600)
    d.Window.frame.blit(d.Window.Plt_C, d.Window.Plt_D)
    d.Window.frame.blit(d.Window.Plt_G, d.Window.Plt_H)

    colors_A = ss.Data.colors 
    colors_B = f.Data.subtitle
    colors_C = colors_B.render(colors_A, True, ss.Data.text, ss.Data.rbg)
    colors_D = colors_C.get_rect()
    colors_D.bottomleft = (50, 450)
    d.Window.frame.blit(colors_C, colors_D)

    d.Window.debug_A = "Press  'D' + 'B' + 'G'  to toggle debug screen"
    d.Window.debug_B = f.Data.scripted
    d.Window.debug_C = d.Window.debug_B.render(d.Window.debug_A, True, ss.Data.text, ss.Data.rbg)
    d.Window.debug_D = d.Window.debug_C.get_rect()
    d.Window.debug_D.bottomleft = (10, 400)
    d.Window.frame.blit(d.Window.debug_C, d.Window.debug_D)

    '''add a notification for the section counter'''
    Data.section_counter_A = 'section counter'      
    Data.section_counter_B = f.Data.scripted
    Data.section_counter_C = Data.section_counter_B.render(Data.section_counter_A, True, ss.Data.text, ss.Data.rbg)
    Data.section_counter_D = Data.section_counter_C.get_rect()
    Data.section_counter_D.bottomleft = (440, 550)
    d.Window.frame.blit(Data.section_counter_C, Data.section_counter_D)
    Data.local_counter_A = str(pni.Data.section_local_counter)
    Data.local_counter_B = f.Data.subtitle
    Data.local_counter_C = Data.local_counter_B.render(Data.local_counter_A, True, ss.Data.text, ss.Data.rbg)
    Data.local_counter_D = Data.section_counter_C.get_rect()
    Data.section_counter_D.bottomleft = (440, 600)
    d.Window.frame.blit(Data.local_counter_C, Data.local_counter_D)

    Data.transcript_copy_A = 'Transcript Copy'
    Data.transcript_copy_B = f.Data.scripted
    Data.transcript_copy_C = Data.transcript_copy_B.render(Data.transcript_copy_A, True, ss.Data.text, ss.Data.rbg)
    Data.transcript_copy_D = Data.transcript_copy_C.get_rect()
    Data.transcript_copy_D.bottomleft = (10, 700)
    d.Window.frame.blit(Data.transcript_copy_C, Data.transcript_copy_D)
    Data.transcript_copy_E = str(pni.Data.transcript_copy)
    Data.transcript_copy_F = f.Data.subtitle
    Data.transcript_copy_G = Data.transcript_copy_F.render(Data.transcript_copy_E, True, ss.Data.text, ss.Data.rbg)
    th.reset_text()
    th.handle_strings(Data.transcript_copy_E, 10, 750, 10, 875, 990, f.Data.subtitle, multiple = 'yes')

