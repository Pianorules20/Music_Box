#gatekeeper.py
import pygame, branches as b, timer as t, debug as db



class Data():

    current_gate = 'pause' #the game must initialize with this value because it is default 'paused'
    info = str('info')
    notes = str('notes')
    
    clock = pygame.time.Clock()
    clock.tick(t.Data.current_timer)
    
    saved_place = 'generate_notes'

    current_gate_function = b.pause()

def testGate():
    info = f' in gatekeeper...{Data.current_gate}'
    print(info)
    #db.Data.debug_log.append(info)

def  passGate(gate):
    
    match gate:
        case 'generate_notes':
    
            Data.current_gate = 'generate_notes'
            b.generator_branches()
            
        case 'plot_notes':
            Data.current_gate = 'plot_notes'
            b.plot_notes()
        
        case 'playback':
            Data.current_gate = 'playback'
            b.playback()
         
        case 'post_production':
            Data.current_gate = 'post_production'
            b.post_production()
        
        case 'pause':
            Data.current_gate = 'pause'
            b.pause()
