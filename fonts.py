#fonts.py
import pygame

class Data():
    pygame.init()
    #note the distinction between font.Font and font.SysFont

    text1 = pygame.font.SysFont('freesans', 30)
    text2 = 'small text'
    scripted = pygame.font.Font('fonts/Callheart.ttf', 45)
    large_script = pygame.font.Font('fonts/Callheart.ttf', 55)
    title =  pygame.font.SysFont('dejavuserif', 40)
    subtitle = pygame.font.SysFont('arplumingtwmbe', 24)
    thick = pygame.font.SysFont('urwbookman', 24)
    small = pygame.font.SysFont('serifyezidi', 30) # see important note below
    thin_tall = pygame.font.SysFont('dejavusansmono', 30)
    snappy = pygame.font.SysFont('c059', 30)
    symbols = pygame.font.SysFont('standardsymbolsps', 30)