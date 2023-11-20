#screens.py
import pygame
import display as d, gatekeeper as g
class Screens():

    current = 'menu'

    def menu():

        d.Window.frame.fill((180, 180, 40),(0,0, d.Window.width, d.Window.height))
        # pygame.draw.rect(d.Window.screen, (100,100,100), (300,800, 100,180), 3,25)
        
        d.Window.spacebar1 = 'Press Spacebar to Create and Record'
        d.Window.myFont = pygame.font.Font('freesansbold.ttf', 24)
        d.Window.spacebar3 = d.Window.myFont.render(d.Window.spacebar1, True, (10,10,20),(200,170,190))
        d.Window.spacebar4 = d.Window.spacebar3.get_rect()
        d.Window.spacebar4.center = (250,200)
        
        d.Window.escape1 = 'Press Escape to Stop'
        d.Window.escape2 = d.Window.myFont
        d.Window.escape3 = d.Window.escape2.render(d.Window.escape1, True, (10,10,20),(200,170,100))
        d.Window.escape4 = d.Window.escape3.get_rect()
        d.Window.escape4.center = (300,400)
        
        d.Window.t1 = 'Press T for console debug'
        d.Window.t2 = d.Window.myFont
        d.Window.t3 = d.Window.t2.render(d.Window.t1, True, (10,10,20), (200, 170, 100))
        d.Window.t4 = d.Window.t3.get_rect()
        d.Window.t4.center = (500, 570)
        
        d.Window.debug1 = f'debug...in {g.Gate.current}'
        d.Window.debug2 = d.Window.myFont
        d.Window.debug3 = d.Window.debug2.render(d.Window.debug1, True, (10,10,20), (200, 170, 190))
        d.Window.debug4 = d.Window.debug3.get_rect()
        d.Window.debug4.center = (650, 650)

        d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)
        d.Window.frame.blit(d.Window.escape3, d.Window.escape4)
        d.Window.frame.blit(d.Window.t3,d.Window.t4)
        d.Window.frame.blit(d.Window.debug3, d.Window.debug4)