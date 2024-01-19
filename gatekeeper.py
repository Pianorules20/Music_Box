#gatekeeper.py
import branches, pygame, timer as t



class Data():

    current = 'pause' #the game must initialize with this value because it is default 'paused'
    info = str('info')
    notes = str('notes')
    
    clock = pygame.time.Clock()
    clock.tick(t.Data.current)
    
    saved_place = 'generate_notes'

    current_function = branches.Branch.pause()

def testGate():
    print(f' in gatekeeper...{Data.current}')

def  passGate(gate):
    
    match gate:
        case 'generate_notes':
    
            Data.current = 'generate_notes'
            branches.Branch.generator_branches()
            
        case 'plot_notes':
            Data.current = 'plot_notes'
            branches.Branch.plot_notes()
        
        case 'playback':
            Data.current = 'playback'
            branches.Branch.playback()
        
        case 'post_production':
            Data.current = 'post_production'
            branches.Branch.post_production()
        
        case 'pause':
            Data.current = 'pause'
            branches.Branch.pause()