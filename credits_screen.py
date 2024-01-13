#credits_screen
import pygame, display as d, display_interface as di, screen_saver as ss, debug as db

class Data():
    initialize = 'initialize'

def credits_screen():

    #db.Data.debug_log.append('credits_screen') artifact me it floods the debug log
    d.Window.frame.fill(ss.Data.rbg,(0,0, di.Data.width, di.Data.height))

    Data.credits_A = 'Credits'
    Data.credits_B = pygame.font.Font('freesansbold.ttf', 40)
    Data.credits_C = Data.credits_B.render(Data.credits_A, True, ss.Data.text, ss.Data.rbg)
    Data.credits_D = Data.credits_C.get_rect()
    Data.credits_D.center = (di.Data.width/2, di.Data.height*0.6)

    Data.msg1_A = '2023-2024 by Bryan Castellucci'
    Data.msg1_B = pygame.font.Font('freesansbold.ttf', 40)
    Data.msg1_C = Data.msg1_B.render(Data.msg1_A, True, ss.Data.text, ss.Data.rbg)
    Data.msg1_D = Data.msg1_C.get_rect()
    Data.msg1_D.center = (di.Data.width/2, di.Data.height*0.65)

    '''blitting'''
    d.Window.frame.blit(Data.credits_C, Data.credits_D)
    d.Window.frame.blit(Data.msg1_C, Data.msg1_D)