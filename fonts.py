#fonts.py
import pygame

class Data():
    #note the distinction between font.Font and font.SysFont

    text1 = pygame.font.SysFont('freesans, 30')
    text2 = 'small text'
    scripted = pygame.font.Font('fonts/Callheart.ttf', 45)
    title =  pygame.font.SysFont('dejavuserif', 40)
    subtitle = pygame.font.SysFont('arplumingtwmbe', 24)
    thick = pygame.font.SysFont('urwbookman', 24)
    small = pygame.font.SysFont('serifyezidi') # see important note below
    thin_tall = pygame.font.SysFont('dejavusansmono', 30)
    snappy = pygame.font.SysFont('c059', 30)
    symbols = pygame.font.SysFont('standardsymbolsps', 30)

#list of available SysFonts...
    
'''    !!! important note !!! the devs seem to have 'hidden' some of the more proprietary fonts with
        an 'noto' prefix to some of the fonts.  This prefix must be removed for them to function although 
        they do not actually function as the fonts themselves rather as a smaller normal font '''

""" 'firamono', 'firasanscompressed', 'dejavuserif', 'arplumingtwmbe', 'notosansthai', 'notosansmodi, \
    'urwbookman', 'notosanspahawhhmong', 'notoserifyezidi', 'notosansoldnortharabian', 'dejavusansmono', \
    'ubuntumono', 'notosanscypriot', 'notosanspsalterpahlavi', 'notosanswarangciti', 'liberationmono',\
    'notosansteluguui', 'firasanscondensed', 'notosanslisu', 'notosansthaiui', 'notosanstamilui', \
    'notosanssogdian', 'notosansmongolian', 'notosanslimbu', 'notoserifcjksc', 'notosansarabicui', \
    'nimbusmonops', 'notosansugaritic', 'notosansmono', 'notosanskhmer', 'notoserifcjktc', \
    'notosansarmenian', 'notosansgujarati', 'freesans', 'p052', 'liberationsansnarrow', \
    'notosansgujaratiui', 'notosansoriya', 'notosanswancho', 'notosanscaucasianalbanian', \
    'notoserifhebrew', 'notosansinscriptionalparthian', 'dejavusans', 'nimbussans', 'arplukaicn', \
    'firasans', 'notosansmayannumerals', 'notosanstakri', 'notosansadlamunjoined', 'notosanssignwriting',\
    'notonaskharabic', 'notosanstifinaghhawad', 'notosanscjkhk', 'liberationsans', 'nimbussansnarrow', \
    'notoseriftelugu', 'arplukaihk', 'notosanscuneiform', 'notorashihebrew', 'notoserifcjkjp', \
    'notoserifcjkhk', 'notoserifcjkkr', 'freeserif', 'c059', 'notosansdevanagariui', 'arplukaitw', \
    'freemono', 'notoseriftamil', 'notosanssyriac', 'notosanscjkjp', 'notosanscjkkr', 'notosanscjktc', \
    'notosanstifinagh', 'notosanssorasompeng', 'notoserifdisplay', 'notosansolchiki', 'robotoslab', \
    'notoserifbalinese', 'notosansmyanmar', 'liberationserif', 'notoserifgurmukhi', 'notoloopedthai', \
    'notosansmarchen', 'notosanssaurashtra', 'ubuntu', 'notoserifahom', 'notoserifbengali', \
    'notosanstifinaghtawellemmet', 'notosanscjksc', 'notosansbamum', 'notosansrunic', 'notoserifkhojki', \
    'notosansnewtailue', 'notosanskannadaui', 'notokufiarabic', 'notosansoldsogdian', 'notoloopedthaiui', \
    'notosansoriyaui', 'notoserifgujarati', 'notoserifarmenian', 'notosanscanadianaboriginal', \
    'notosansbalinese', 'notosans', 'notosanstifinaghair', 'z003', 'urwgothic', 'notosansbhaiksuki', \
    'notoserifkhmer', 'notosansjavanese', 'notoserifmalayalam', 'notosansdisplay', 'notosanslinearb', \
    'notosanskannada', 'notosanslycian', 'notosansshavian', 'notosansbengali', 'notosanskhudawadi', \
    'notosansyi', 'notosanslineara', 'notosansinscriptionalpahlavi', 'd050000l', 'notoserifdogra', \
    'notosanslydian', 'notosanstagalog', 'notosansosmanya', 'notosanshanunoo', 'notosansdevanagari', \
    'notosansmeeteimayek', 'notoserifgrantha', 'notosanskhmerui', 'notosansethiopic', \
    'notosansoldsoutharabian', 'notosanselbasan', 'notoserifmyanmar', 'notosansgeorgian', \
    'notoseriftangut', 'notosanstifinaghadrar', 'notosanslaoui', 'notosansgrantha', 'notosansbassavah', \
    'nimbusroman', 'notoloopedlaoui', 'notosansgurmukhiui', 'notoserifethiopic', 'notosansgurmukhi', \
    'notoserifsinhala', 'opensymbol', 'notosanskharoshthi', 'notosansrejang', 'notosansmedefaidrin', \
    'notosanssinhalaui', 'notoserifhmongnyiakeng', 'notoserif', 'notosansnushu', 'droidsansfallback', \
    'notoserifdevanagari', 'notosanstaiviet', 'notosansduployan', 'notosansbuhid', 'notosansthaana', \
    'notosansmro', 'notosanstamil', 'notosanskayahli', 'notosansnko', 'notosansdeseret', \
    'notosanssundanese', 'notosansosage', 'notosanscham', 'notosanstifinaghazawagh', \
    'notoseriftamilslanted', 'notosanslepcha', 'notosanslao', 'notosansmiao', 'notosanstifinaghapt', \
    'notosanshanifirohingya', 'notosansmyanmarui', 'notoserifgeorgian', 'notosansmalayalamui', \
    'notosansoldturkic', 'notoseriflao', 'notosansnewa', 'notomusic', 'notosansegyptianhieroglyphs', \
    'notosansimperialaramaic', 'notosansmath', 'notosanstirhuta', 'notosanstifinaghghat', \
    'notosansbuginese', 'notosansolditalic', 'notoserifthai', 'nototraditionalnushu', \
    'notosansmasaramgondi', 'notosanssylotinagri', 'notosansbengaliui', 'notosansavestan', \
    'notosanssinhala', 'notosansoldpermic', 'notosanspalmyrene', 'notosansmalayalam', 'notosanskhojki', \
    'notonaskharabicui', 'notonastaliqurdu', 'notosanssoyombo', 'notosanspaucinhau', 'notosansgothic', \
    'notosanssamaritan', 'notosanscoptic', 'notosanskaithi', 'notosanstagbanwa', 'notosansadlam', \
    'notosansmeroitic', 'notosansmonocjktc', 'notoserifkannada', 'notosanstifinaghahaggar', \
    'notosansmonocjksc', 'notosansgunjalagondi', 'notosansmonocjkkr', 'notosansmonocjkhk', \
    'notosansarabic', 'notosansmonocjkjp', 'notosanstamilsupplement', 'arplukaitwmbe', \
    'notosansoldpersian', 'notosansanatolianhieroglyphs', 'notosanssymbols2', 'notosansmanichaean', \
    'notoloopedlao', 'notosansbatak', 'notosanssharada', 'notosanstaitham', 'arplumingtw', \
    'notosanshatran', 'ubuntucondensed', 'notosansmultani', 'standardsymbolsps', 'arplumingcn', \
    'notosanscarian', 'notomono', 'notosanschakma', 'arpluminghk', 'notoseriftibetan', \
    'notosanszanabazarsquare', 'notosanscherokee', 'notosansbrahmi', 'notosanssymbols', \
    'notosansmendekikakui', 'notosansvai', 'notosanselymaic', 'notosanstelugu', 'notocoloremoji', \
    'notosanshebrew', 'notosansmandaic', 'notosansmahajani', 'notosansoldhungarian', \
    'notosansindicsiyaqnumbers', 'notosanstifinaghsil', 'notosanssiddham', 'notosansogham', \
    'notosanstaile', 'notosansphagspa', 'notosansphoenician', 'notosanstifinaghagrawimazighen', \
    'notosanstifinaghrhissaixa', 'notosansglagolitic', 'notosansnabataean' """