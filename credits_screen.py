#credits_screen
import display as d, screen_saver as s_s, fonts as f, layout_menu_style as lm, text_handler as th

class Data():
    initialize = 'initialize'

def credits_screen():

    #db.Data.debug_log.append('credits_screen') artifact me it floods the debug log
    d.Data.window.fill(s_s.Data.rbg,(0,0, lm.Data.width, lm.Data.height))

    Data.credits_A = 'Credits'
    Data.credits_B = f.Data.title
    Data.credits_C = Data.credits_B.render(Data.credits_A, True, s_s.Data.text, s_s.Data.rbg)
    Data.credits_D = Data.credits_C.get_rect()
    Data.credits_D.center = lm.Data.header
    d.Data.window.blit(Data.credits_C, Data.credits_D)

    Data.msg1_A = '2023-2024 by Bryan Castellucci'
    Data.msg1_B = f.Data.title
    Data.msg1_C = Data.msg1_B.render(Data.msg1_A, True, s_s.Data.text, s_s.Data.rbg)
    Data.msg1_D = Data.msg1_C.get_rect()
    Data.msg1_D.center = lm.Data.header_2
    d.Data.window.blit(Data.msg1_C, Data.msg1_D)

    '''Data.transcript_copy_A = 'Transcript Copy'
    Data.transcript_copy_B = f.Data.scripted
    Data.transcript_copy_C = Data.transcript_copy_B.render(Data.transcript_copy_A, True, ss.Data.text, ss.Data.rbg)
    Data.transcript_copy_D = Data.transcript_copy_C.get_rect()
    Data.transcript_copy_D.bottomleft = (10, 700)
    d.Data.window.blit(Data.transcript_copy_C, Data.transcript_copy_D)'''
    '''Data.transcript_copy_E = str(pni.Data.transcript_copy)
    Data.transcript_copy_F = f.Data.subtitle
    Data.transcript_copy_G = Data.transcript_copy_F.render(Data.transcript_copy_E, True, ss.Data.text, ss.Data.rbg)'''
    Data.thanks_A = 'Thanks to the Pygame community, the Stack Overflow devs  and the Real Python team'
    Data.thanks_B = f.Data.scripted
    Data.thanks_C = Data.thanks_B.render(Data.thanks_A, True, s_s.Data.text, s_s.Data.rbg)
    Data.thanks_D = Data.thanks_C.get_rect()
    Data.thanks_D.center = (lm.Data.x1000, lm.Data.y500)
    d.Data.window.blit(Data.thanks_C, Data.thanks_D)
    Data.special_thanks_A = "A   special   thanks   to   Joshua   Castellucci   for   always   believing  \
          in   me   and   for  \
          steering   me   in   the   direction   of   programming."
    th.reset_text()
    th.handle_strings(Data.special_thanks_A, 200, 700, 200, 1650, 990, f.Data.scripted, auto_scroll = 'no')
