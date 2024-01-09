#screens.py
import pygame
import display as d, gatekeeper as g, debug as db, display_interface as di
class Screens():

    current = 'menu'

    def menu():

        d.Window.frame.fill((180, 180, 40),(0,0, di.I.width, di.I.height))
        # pygame.draw.rect(d.Window.screen, (100,100,100), (300,800, 100,180), 3,25)
        
        d.Window.spacebar1 = 'Press Spacebar to Create and Record'
        d.Window.myFont = pygame.font.Font('freesansbold.ttf', 24)
        d.Window.spacebar3 = d.Window.myFont.render(d.Window.spacebar1, True, (10,10,20),(200,170,190))
        d.Window.spacebar4 = d.Window.spacebar3.get_rect()
        d.Window.spacebar4.center = (di.I.width/10, di.I.height*0.9)
        
        d.Window.escape1 = 'Press Escape to Stop'
        d.Window.escape2 = d.Window.myFont
        d.Window.escape3 = d.Window.escape2.render(d.Window.escape1, True, (10,10,20),(200,170,100))
        d.Window.escape4 = d.Window.escape3.get_rect()
        d.Window.escape4.center = (di.I.width/10, di.I.height*0.8)
        
        d.Window.t1 = 'Press T for debug trace'
        d.Window.t2 = d.Window.myFont
        d.Window.t3 = d.Window.t2.render(d.Window.t1, True, (10,10,20), (200, 170, 100))
        d.Window.t4 = d.Window.t3.get_rect()
        d.Window.t4.center = (di.I.width/10, di.I.height*0.7)
        d.Window.t_A = db.tracer4
        d.Window.t_B = d.Window.myFont
        d.Window.t_C = d.Window.t_B.render(d.Window.t_A, True, (10,10,20), (200,200,100))
        d.Window.t_D = d.Window.t_C.get_rect()
        d.Window.t_D.center = (di.I.width/10, di.I.height*0.73)

        d.Window.gate_A = 'gate'
        d.Window.gate_B = d.Window.myFont
        d.Window.gate_C = d.Window.gate_B.render(d.Window.gate_A, True, (10,10,20), (200,170,100))
        d.Window.gate_D = d.Window.gate_C.get_rect()
        d.Window.gate_D.center = (di.I.width/9.5, di.I.height*0.57) 
        d.Window.tracer1a = db.tracer1
        d.Window.tracer1b = d.Window.myFont
        d.Window.tracer1c = d.Window.tracer1b.render(d.Window.tracer1a, True, (10,10,20), (200, 200, 100))
        d.Window.tracer1d = d.Window.tracer1c.get_rect()
        d.Window.tracer1d.center = (di.I.width/10, di.I.height*0.6)

        d.Window.C_S_A = 'current section notes'
        d.Window.C_S_B = d.Window.myFont
        d.Window.C_S_C = d.Window.C_S_B.render(d.Window.C_S_A, True, (10,10,20), (200,200,100))
        d.Window.C_S_D = d.Window.C_S_C.get_rect()
        d.Window.C_S_D.center = (di.I.width/9.5, di.I.height*0.32)
        d.Window.tracer2a = db.tracer2  
        d.Window.tracer2b = d.Window.myFont
        d.Window.tracer2c = d.Window.tracer2b.render(d.Window.tracer2a, True, (10,10,20), (200,170,100))
        d.Window.tracer2d = d.Window.tracer2c.get_rect()
        d.Window.tracer2d.center = (di.I.width/10, di.I.height*0.35)

        d.Window.Trn_A = 'transcript notes'
        d.Window.Trn_B = d.Window.myFont
        d.Window.Trn_C = d.Window.Trn_B.render(d.Window.Trn_A, True, (10,10,20), (200,200,100))
        d.Window.Trn_D = d.Window.Trn_C.get_rect()
        d.Window.Trn_D.center = (di.I.width/9.5, di.I.height*0.07)
        d.Window.tracer3a = db.tracer3
        d.Window.tracer3b = d.Window.myFont
        d.Window.tracer3c = d.Window.tracer3b.render(d.Window.tracer3a, True, (10,10,20), (200,170,100))
        d.Window.tracer3d = d.Window.tracer3c.get_rect()
        d.Window.tracer3d.center = (di.I.width/10, di.I.height*0.1)

        '''blitting'''
        d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)
        d.Window.frame.blit(d.Window.escape3, d.Window.escape4)
        
        d.Window.frame.blit(d.Window.t3,d.Window.t4)
        d.Window.frame.blit(d.Window.t_C, d.Window.t_D)

        d.Window.frame.blit(d.Window.gate_C, d.Window.gate_D)
        d.Window.frame.blit(d.Window.tracer1c, d.Window.tracer1d)
        
        d.Window.frame.blit(d.Window.C_S_C, d.Window.C_S_D)
        d.Window.frame.blit(d.Window.Trn_C, d.Window.Trn_D)

        d.Window.frame.blit(d.Window.tracer2c, d.Window.tracer2d)
        d.Window.frame.blit(d.Window.tracer3c, d.Window.tracer3d)