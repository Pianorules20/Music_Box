#plot_notes.py
import my_song as m_s, playback as pb, display_interface as d_i, settings as s
import debug as db, gatekeeper as g, pni

class Data():
   
    counter = s.Data.metronome
    section_counter = int(0)
    populate_copy = True
    plot_meter = int(0)

def reset_counter():
    Data.counter = int(0)
    
def plot_notes():
    #careful Bryan!!! Make certain that you reset your meter if necessary and or get your sections correct

    info = f'transcript_{m_s.Data.transcript}'
    print(info)    
    db.Data.debug_log.append(info)

    if Data.populate_copy == True:
        pb.Data.final_copy = m_s.Data.transcript
        Data.populate_copy = not Data.populate_copy
        info = f'plot_nots populate_copy = False. final_copy {pb.Data.final_copy}'
        print(info)
        db.Data.debug_log.append(info)

    
    else:

        if len(pb.Data.final_copy[Data.section_counter]) > 0:
            info = f'p_n_len_final_copy_this_section_{pb.Data.final_copy[Data.section_counter]}'
            print(info)
            db.Data.debug_log.append(info)
            
            for eachNote in pb.Data.final_copy[Data.section_counter]:
                if Data.plot_meter >= eachNote.xPos:
                    pni.Data.current_plot.append(eachNote)
                else: 
                    pass

            pni.create_plot()
            Data.counter += 1

        else:
            pass
    pb.Data.note_count = Data.counter
    pb.Data.note_count = Data.counter
    reset_counter()
    g.Data.current_gate = 'playback'
    d_i.Data.current_screen =  'playback'
    Data.populate_copy = not Data.populate_copy


'''This file works primarily with 'pni' class 'Count' variables are sectionCounter, noteCounter and populate *bool*'''
'''class P():
     pass #'Pl' stands for 'Plot'''
'''
def plot_notes(): 

    
        # referencing pm.M.meter
    if pni.Data.populate_me == True:
            
            db.Data.debug_log.append(f'pni.populate_me = {pni.Data.populate_me}')
            pni.populateNotes()

    else:
        pass

    for eachNote in pni.Data.this_section: 

        xPos = gni.Note.returnXPos(eachNote)

        if pm.M.meter == xPos:

            pni.Data.current_plot.append(eachNote)  # pay attention!!!  This is what the playback will use
            try:
                    
                pni.Data.section_counter -= 1

            except:
                
                pni.advance()

        else:
            
            pass
    
    pni.createPlot(notesExternal = pni.Data.current_plot)
    
    pni.resetPlot()

        #gatekeeper.Gate.current = 'plot_notes'
    else:
        print('error in plot_notes? what happened to Count.note Counter?')
        try: 
                pni.I.sectionCounter +=1
        except:
            pni.I.populateMe != pni.I.populateMe
            gatekeeper.Gate.current = 'playback'''


        
'''class Note(pygame.sprite.Sprite):

    counter = 0
    note = pygame.sprite.Sprite()
    note = pygame.Surface((0,0))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen
    
    def __init__(self, frame, x_plot, y_plot) -> None:
        print('Player Object Initiated')
        pygame.sprite.Sprite.__init__(self)
        self.frame = frame
        self.image = pygame.Surface((0,0))
        self.image = pygame.image.load(frame).convert()
        self.rect = self.image.get_rect()
        Note.note = self.image
        self.x_plot = x_plot
        self.y_plot = y_plot
        #Player.face_right = Player.hero
        Note.position = (self.x_plot, self.y_plot)
        display.Window.position= Note.position
        #create.py should handle inputting a new surface into the Window.note position
        Note.rect = self.rect 
    def returnData():
       return Note.note, Note.position
    
    def _blit_():
       display.Window.frame.blit(Note.note, Note.position)'''