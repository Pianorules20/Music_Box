#debug.py
import display as d, mySong as my, gatekeeper as g, structure as struc
import screen_saver as ss, text_handler as th, fonts as f, layout_menu_style as lm, playback as pb

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
    d.Data.frame.fill(ss.Data.rbg, lm.Data.frame_data)
    # pygame.draw.rect(d.Data.screen, (100,100,100), (300,800, 100,180), 3,25)

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
    d.Data.frame.blit(Data.myFontsC, Data.myFontsD)
    if Data.fonts_gate == True:
        print(Data.myFontsA)
        Data.fonts_gate = False
    else:
        pass'''

    d.Data.splash_A = 'DEBUG SCREEN'
    d.Data.splash_B = f.Data.title
    d.Data.splash_C = d.Data.splash_B.render(d.Data.splash_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.splash_D = d.Data.splash_C.get_rect()
    d.Data.splash_D.center = lm.Data.header
    d.Data.frame.blit(d.Data.splash_C, d.Data.splash_D)

    Data.song_finished_A = 'Is Song Finished?'
    Data.song_finished_B = f.Data.scripted
    Data.song_finished_C = Data.song_finished_B.render(Data.song_finished_A, True, ss.Data.text, ss.Data.rbg)
    Data.song_finished_D = Data.song_finished_C.get_rect()
    Data.song_finished_D.center = lm.Data.x1000, lm.Data.y300
    d.Data.frame.blit(Data.song_finished_C, Data.song_finished_D)
    Data.song_finished_E = str(my.Data.song_finished)
    Data.song_finished_F = f.Data.subtitle
    Data.song_finished_G = Data.song_finished_F.render(Data.song_finished_E, True, ss.Data.text, ss.Data.rbg)
    Data.song_finished_H = Data.song_finished_G.get_rect()
    Data.song_finished_H.center = lm.Data.x1000, lm.Data.y400
    d.Data.frame.blit(Data.song_finished_G, Data.song_finished_H)


    d.Data.spacebar1 = 'Press Spacebar to Create and Record'
    d.Data.spacebar2 = f.Data.scripted
    d.Data.spacebar3 = d.Data.spacebar2.render(d.Data.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Data.spacebar4 = d.Data.spacebar3.get_rect()
    d.Data.spacebar4.bottomleft = (lm.Data.x10, lm.Data.y50)
    d.Data.frame.blit(d.Data.spacebar3, d.Data.spacebar4)
         
    d.Data.escape1 = 'Press Escape to Stop'
    d.Data.escape2 = f.Data.scripted
    d.Data.escape3 = d.Data.escape2.render(d.Data.escape1, True, ss.Data.text, ss.Data.rbg)
    d.Data.escape4 = d.Data.escape3.get_rect()
    d.Data.escape4.bottomleft = (lm.Data.x10, lm.Data.y100)
    d.Data.frame.blit(d.Data.escape3, d.Data.escape4)

    Data.trace_A = 'Press T for debug trace'
    Data.trace_B = f.Data.scripted
    Data.trace_C = Data.trace_B.render(Data.trace_A, True, ss.Data.text, ss.Data.rbg)
    Data.trace_D = Data.trace_C.get_rect()
    Data.trace_D.bottomleft = (lm.Data.x10, lm.Data.y150)
    Data.trace_E = Data.debug_log[-1]
    Data.trace_F = f.Data.subtitle
    Data.trace_G = Data.trace_F.render(Data.trace_E, True, ss.Data.text, ss.Data.rbg)
    Data.trace_H = Data.trace_G.get_rect()
    Data.trace_H.bottomleft = (lm.Data.x40+10, lm.Data.y200-20)
    d.Data.frame.blit(Data.trace_C, Data.trace_D)
    if Data.debug_trace == True:    
        d.Data.frame.blit(Data.trace_G, Data.trace_H)
    else:
        pass

    Data.log_A = "Press 'L' + 'G'for Debug Log"
    Data.log_B = f.Data.scripted
    Data.log_C = Data.log_B.render(Data.log_A, True, ss.Data.text, ss.Data.rbg)
    Data.log_D = Data.log_C.get_rect()
    Data.log_D.bottomleft = (lm.Data.x10, lm.Data.y250)
    d.Data.frame.blit(Data.log_C, Data.log_D)

    d.Data.gate_A = 'Gate'
    d.Data.gate_B = f.Data.scripted
    d.Data.gate_C = d.Data.gate_B.render(d.Data.gate_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.gate_D = d.Data.gate_C.get_rect()
    d.Data.gate_D.bottomleft = (lm.Data.x10, lm.Data.y300)
    d.Data.tracer1a = g.Data.current_gate
    d.Data.tracer1b = f.Data.subtitle
    d.Data.tracer1c = d.Data.tracer1b.render(d.Data.tracer1a, True, ss.Data.text, ss.Data.rbg)
    d.Data.tracer1d = d.Data.tracer1c.get_rect()
    d.Data.tracer1d.bottomleft = (lm.Data.x40+10, lm.Data.y350-20)
    d.Data.frame.blit(d.Data.gate_C, d.Data.gate_D)
    d.Data.frame.blit(d.Data.tracer1c, d.Data.tracer1d)

    d.Data.C_S_A = 'current section notes'
    d.Data.C_S_B = f.Data.scripted
    d.Data.C_S_C = d.Data.C_S_B.render(d.Data.C_S_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.C_S_D = d.Data.C_S_C.get_rect()
    d.Data.C_S_D.bottomleft = (lm.Data.x10, lm.Data.y400)
    d.Data.frame.blit(d.Data.C_S_C, d.Data.C_S_D)
    d.Data.tracer2a = str(f'currentsection = {my.Data.current_section}')
    d.Data.tracer2b = f.Data.subtitle
    d.Data.tracer2c = d.Data.tracer2b.render(d.Data.tracer2a, True, ss.Data.text, ss.Data.rbg)
    #d.Data.tracer2d = d.Data.tracer2c.get_rect()
    th.reset_text()
    th.handle_strings(d.Data.tracer2a, lm.Data.x1000, lm.Data.y450, lm.Data.x1000, lm.Data.x2000-10, \
                      lm.Data.y900, f.Data.subtitle, multiple = 'yes')

    d.Data.Plt_A = 'plotted notes'
    d.Data.Plt_B = f.Data.scripted
    d.Data.Plt_C = d.Data.Plt_B.render(d.Data.Plt_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.Plt_D = d.Data.Plt_C.get_rect()
    d.Data.Plt_D.bottomleft = (lm.Data.x10, lm.Data.y550-30)
    d.Data.frame.blit(d.Data.Plt_C, d.Data.Plt_D)
    
    d.Data.Plt_E = str(f'in_debug.py,_pointing_at_structure.py_Data.save_place_{struc.Data.save_place}')
    print(d.Data.Plt_E)
    Data.debug_log.append(d.Data.Plt_E)
    d.Data.Plt_F = f.Data.subtitle
    d.Data.Plt_G = d.Data.Plt_F.render(d.Data.Plt_E, True, ss.Data.text, ss.Data.rbg)
    d.Data.Plt_H = d.Data.Plt_G.get_rect()
    d.Data.Plt_H.bottomleft = (lm.Data.x40+10, lm.Data.y600-30)
    d.Data.frame.blit(d.Data.Plt_G, d.Data.Plt_H)

    colors_A = ss.Data.colors 
    colors_B = f.Data.subtitle
    colors_C = colors_B.render(colors_A, True, ss.Data.text, ss.Data.rbg)
    colors_D = colors_C.get_rect()
    colors_D.bottomleft = (lm.Data.x40+10, lm.Data.y450)
    d.Data.frame.blit(colors_C, colors_D)

    d.Data.debug_A = "Press  'D' + 'B' + 'G'  to toggle debug screen"
    d.Data.debug_B = f.Data.scripted
    d.Data.debug_C = d.Data.debug_B.render(d.Data.debug_A, True, ss.Data.text, ss.Data.rbg)
    d.Data.debug_D = d.Data.debug_C.get_rect()
    d.Data.debug_D.bottomleft = (lm.Data.x10, lm.Data.y400)
    d.Data.frame.blit(d.Data.debug_C, d.Data.debug_D)

    '''add a notification for the section counter'''
    Data.section_counter_A = 'section counter'      
    Data.section_counter_B = f.Data.scripted
    Data.section_counter_C = Data.section_counter_B.render(Data.section_counter_A, True, ss.Data.text, ss.Data.rbg)
    Data.section_counter_D = Data.section_counter_C.get_rect()
    Data.section_counter_D.bottomleft = (lm.Data.x500-60, lm.Data.y550-30)
    d.Data.frame.blit(Data.section_counter_C, Data.section_counter_D)
    
                      
    '''Data.local_counter_A = str(pni.Data.section_local_counter)
    Data.local_counter_B = f.Data.subtitle
    Data.local_counter_C = Data.local_counter_B.render(Data.local_counter_A, True, ss.Data.text, ss.Data.rbg)
    Data.local_counter_D = Data.section_counter_C.get_rect()
    Data.section_counter_D.bottomleft = (lm.Data.x500-10, lm.Data.y600)
    d.Data.frame.blit(Data.local_counter_C, Data.local_counter_D)'''

    Data.transcript_copy_A = 'Transcript Copy'
    Data.transcript_copy_B = f.Data.scripted
    Data.transcript_copy_C = Data.transcript_copy_B.render(Data.transcript_copy_A, True, ss.Data.text, ss.Data.rbg)
    Data.transcript_copy_D = Data.transcript_copy_C.get_rect()
    Data.transcript_copy_D.bottomleft = (lm.Data.x10, lm.Data.y700)
    d.Data.frame.blit(Data.transcript_copy_C, Data.transcript_copy_D)
    Data.transcript_copy_E = str(my.Data.transcript)
    Data.transcript_copy_F = f.Data.subtitle
    Data.transcript_copy_G = Data.transcript_copy_F.render(Data.transcript_copy_E, True, ss.Data.text, ss.Data.rbg)
    th.reset_text()
    th.handle_strings(Data.transcript_copy_E, lm.Data.x10, lm.Data.y750, lm.Data.x10, lm.Data.x900-25, lm.Data.y1000-10, f.Data.subtitle, multiple = 'yes')