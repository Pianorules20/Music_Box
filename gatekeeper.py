#gatekeeper.py
import branches as b



class Data():

    pause: str = 'pause'
    generate_notes: str = 'generate_notes'
    plot_notes: str = 'plot_notes'
    playback: str = 'playback'
    post_production: str = 'post_production'
    
    current_gate: str = pause #the game must initialize with this value because it is default 'paused'
    
    info: str = 'info'
    notes: str = 'notes'
    
    saved_place:str = 'generate_notes'

    current_gate_function = b.pause()

def testGate(): 
    info = f' in gatekeeper...{Data.current_gate}'
    print(info)
    #db.Data.debug_log.append(info)

def passGate(gate):

    match Data.current_gate:
        case Data.generate_notes:
    
            print('in gatekeeper entering branch.generator_branches()')
            b.generator_branches()
            
        case Data.plot_notes:
            b.plot_notes()
        
        case Data.playback:
            b.playback()
            
        case Data.post_production:
            b.post_production()
        
        case Data.pause:
            b.pause()