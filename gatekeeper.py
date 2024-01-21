#gatekeeper.py
import pygame, branches as b, timer as t



class Data():

    current = 'pause' #the game must initialize with this value because it is default 'paused'
    info = str('info')
    notes = str('notes')
    
    clock = pygame.time.Clock()
    clock.tick(t.Data.current)
    
    saved_place = 'generate_notes'

    current_function = b.pause()

def testGate():
    print(f' in gatekeeper...{Data.current}')

def  passGate(gate):
    
    match gate:
        case 'generate_notes':
    
            Data.current = 'generate_notes'
            b.generator_branches()
            
        case 'plot_notes':
            Data.current = 'plot_notes'
            b.plot_notes()
        
        case 'playback':
            Data.current = 'playback'
            b.playback()
         
        case 'post_production':
            Data.current = 'post_production'
            b.post_production()
        
        case 'pause':
            Data.current = 'pause'
            b.pause()