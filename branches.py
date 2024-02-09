#mainBranch.py
import settings as s, structure as struc, plot_notes as pn, playback as pb, post_production as pp, debug as db
import mySong as my

class Branch():
    pass

def generator_branches():
    if s.Data.structure == 'Random Short Form':
        struc.randomShortForm()
    elif s.Data.structure == 'Long Form New':
        struc.longFormNew()
    elif s.Data.structure == 'User Constructed': #catches settings 'User Constructed'
        struc.userConstructed()
    else:
        db.debug_log.append('Error in branches.Branch...re: settings.Data.structure')

def plot_notes():
    pn.plot_notes()

def playback():
    pb.play()

def post_production():

    pp.print_sheet()
    pp.record_audio()
    if s.Data.repeat_composition == False:
        pass
    else:
        pp.new_instance()
def pause():
    pass