import settings, mySong, instance, tones, pygame.mixer, display

class Note():

    note = pygame.Surface((0,0))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen

    def __init__(self, frame, xPos, yPos, sound, duration, letterName, octave, instrument, polyOrder, \
                 image) -> None:
        print('Player Object Initiated')
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
        self.image = image 
        #Player.face_right = Player.hero
        Note.position = (self.x_plot, self.y_plot)
        display.Window.position= Note.position
        #create.py should handle inputting a new surface into the Window.note position
        Note.rect = self.rect 
   
    def returnSound(self):
        return self.sound

    def returnData():
       return Note.note, Note.position
    
    def returnXPos(self):
        return self.xPos 
    
    def _blit_():
       display.Window.frame.blit(Note.note, Note.position)
    
    def play(x):
        pygame.mixer.find_channel(True)
        pygame.mixer.Sound.play(x)

def createNote(currentNote, currentDuration):
    name = tones.Tone.returnLetterName(currentNote)
    octave = tones.Tone.returnOctave(currentNote)
    xPos = mySong.Transcription.meter
    height = tones.Tone.returnClefHeight(currentNote)
    sound = tones.Tone.returnSound(currentNote)
    music = Note(sound = sound, duration = currentDuration, \
        letterName = name, octave = octave, \
            instrument =  settings.Preferences.instrument1, polyOrder = settings.Preferences.polyOrderList[0], \
        image = 'images/quarterNoteCorrect.png', xPos = mySong.Transcription.meter, \
            yPos = height)
    mySong.Transcription.currentSection.append(music)
    mySong.Transcription.meter += currentDuration
        #this is where i blit to a surface??
    instance.notesRemaining -= 1
    '''except Exception as e:
            print('error in step3 early randomizer with settings...')
            print(e)'''
    print(f' in primeInterface: Note spacial data xPos {xPos} {name}{octave} yPos{height}')
    print(f' in interface: instance.notesRemaining = {instance.notesRemaining}')