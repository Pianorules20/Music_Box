#mainBranch.py
import settings as s, branches2, plot_notes as pn, playback as pb, post_production as pp, debug as db, mySong as my

class Branch():
    pass

def generator_branches():
    if s.Data.structure == 'Random Short Form':
        branches2.randomShortForm()
    elif s.Data.structure == 'Long Form New':
        branches2.longFormNew()
    elif s.Data.structure == 'User Constructed': #catches settings 'User Constructed'
        branches2.userConstructed()
    else:
        db.debug_log.append('Error in branches.Branch...re: settings.Op.structure')

def plot_notes():
    pn.plot_notes()

def playback():
    pb.play()

def post_production():

    pp.print_sheet()
    pp.record_audio()
    my.reset_transcript()

def pause():
    pass