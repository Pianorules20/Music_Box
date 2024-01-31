#gni means 'generate notes interface'
import settings as s, mySong, current_section as cs, tones as t, pygame.mixer, display as d, debug as db

class Note():

    note = pygame.Surface((0,0))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen

    def __init__(self, frame, xPos, yPos, sound, duration, letterName, octave, instrument, polyOrder) -> None:
        print('in gni class Note')
        pygame.sprite.Sprite.__init__(self)
        self.frame = frame
        self.image = pygame.Surface((0,0))
        self.image = pygame.image.load(frame).convert()
        self.rect = self.image.get_rect()
        Note.image = self.image
        self.xPos = xPos
        self.yPos = yPos
        self.sound = sound
        self.duration = duration
        self.letterName = letterName
        self.octave = octave
        self.instrument = instrument
        self.polyOrder = polyOrder
        #Player.face_right = Player.hero
        Note.position = (self.xPos, self.yPos)
        d.Data.position= Note.position
        #create.py should handle inputting a new surface into the Data.note position
        Note.rect = self.rect 
   
    def returnLetterName(self):
        return self.letterName
    
    def returnOctave(self):
        return self.octave

    def returnSound(self):
        return self.sound

    def returnData():
       return Note.note, Note.position
    
    def returnXPos(self):
        return self.xPos 
    
    def returnRect(self):
        return self.rect
    
    def _blit_():
       d.Data.frame.blit(Note.note, Note.position)
    
    def play(x):
        pygame.mixer.find_channel(True)
        pygame.mixer.Sound.play(x)  

def createNote(currentNote, currentDuration):
    name = t.Tone.returnLetterName(currentNote)
    octave = t.Tone.returnOctave(currentNote)
    xPos = mySong.Data.meter
    height = t.Tone.returnClefHeight(currentNote)
    sound = t.Tone.returnSound(currentNote)
    music = Note(sound = sound, duration = currentDuration, \
        letterName = name, octave = octave,\
            instrument =  s.Data.instrument1, polyOrder = s.Data.polyOrderList[0], \
        frame = 'images/quarterNoteCorrect.png', xPos = mySong.Data.meter, \
            yPos = height)
    cs.Data.current_section.append(music)
    #mySong.Data.current_section.append(music)
    mySong.Data.meter += currentDuration
        #this is where i blit to a surface??
    cs.Data.notesRemaining -= 1
    '''except Exception as e:
            print('error in step3 early randomizer with settings...')
            print(e)'''
    db.Data.debug_log.append(f' in gni: Note spacial data xPos {xPos} {name}{octave} yPos{height}')
    db.Data.debug_log.append(f' instance.notesRemaining = {cs.Data.notesRemaining}')
    # breadcrumb print(f' in gni: Note spacial data xPos {xPos} {name}{octave} yPos{height}') 
    # breadcrumb print(f' instance.notesRemaining = {instance.notesRemaining}')