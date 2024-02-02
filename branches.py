#mainBranch.py
import settings as s, structure as struc, plot_notes as pn, playback as pb, post_production as pp, debug as db
import mySong as my

class Branch():
    pass

def generator_branches():
    if s.Data.struc == 'Random Short Form':
        struc.randomShortForm()
    elif s.Data.struc == 'Long Form New':
        struc.longFormNew()
    elif s.Data.struc == 'User Constructed': #catches settings 'User Constructed'
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
    pp.new_instance()

def pause():
    pass