#gatekeeper.py
import branches, pygame, timer as t



class Gate():

    clock = pygame.time.Clock()
    clock.tick(t.Timer.current)

    current = 'pause' #the game must initialize with this value because it is default 'paused'
    
    saved_place = 'generate_notes'

    current_function = branches.Branch.pause()

    def testGate():
        print(f' in gatekeeper...{Gate.current}')

    def  passGate(gate):
        match gate:
            case 'generate_notes':
        
                Gate.current = 'generate_notes'
                branches.Branch.generator_branches()
                
            case 'plot_notes':
                Gate.current = 'plot_notes'
                branches.Branch.plot_notes()
           
            case 'playback':
                Gate.current = 'playback'
                branches.Branch.playback()
           
            case 'post_production':
                Gate.current = '_post_production'
                branches.Branch.post_production()
           
            case 'pause':
                Gate.current = 'pause'
                branches.Branch.pause()
        return gate