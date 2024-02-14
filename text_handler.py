#textHandler.py
import screen_saver as s_s, display as d, layout_menu_style as l_m

class Data():
    #use the individual screens to update the Data.text
    start = 20
    xAxis = 20
    yAxis = 650
    offset = 0
    #right_edge = 0
    color_counter = int(0)
    current_color = s_s.Data.text
    multi_colors = s_s.Data.color_list
    scroll_pages = False

'''def advance():
    
    Data.multi_colors.append(Data.multi_colors[0])
    Data.multi_colors.pop(0)'''

def reset_text():
    Data.start = 20
    Data.xAxis = 20
    Data.yAxis = 650
    Data.offset = 0
    Data.color_counter = int(0)
    Data.current_color = s_s.Data.text
    #di.Data.scroll_pages = False

def scroll_page():
    d.Data.background = d.Data.frame.fill((180,180,40),(0,0, d.Data.width, d.Data.height))
    for each in l_m.Data.y_values:
        each -= 900
        

def scroll_reset():
    for each in l_m.Data.y_values:
        each = l_m.Data.originalY[each]

def handle_strings(myText, xAxis, yAxis, leftEdge, rightEdge, bottomEdge, font, auto_scroll):
    Data.text = myText
    Data.word = Data.text.split(' ')
    Data.start = xAxis
    Data.xAxis = Data.start
    Data.yAxis = yAxis
    Data.offset = 0
    Data.scroll_offset = -900
    for eachWord in Data.word:
        Data.xAxis += Data.offset
        textA = eachWord
        textB = font
        textC = textB.render(textA, True, Data.current_color, s_s.Data.rbg)
        Data.offset = textC.get_width()
        if Data.xAxis > rightEdge:
            Data.xAxis = leftEdge
            Data.yAxis += 50
        else:
            pass
        if Data.yAxis > bottomEdge:
            if auto_scroll == 'yes':
                d.Data.frame.fill(s_s.Data.rbg)
                Data.xAxis = leftEdge
                Data.yAxis = yAxis
                Data.current_color = Data.multi_colors[1]
            else:
                pass
        else:
            pass
        textD = textC.get_rect()    
        textD.bottomleft = (Data.xAxis, Data.yAxis)
        d.Data.frame.blit(textC, textD)

'''
     d.Window.spacebar1 = 'Press Spacebar to Create and Record'
    d.Window.spacebar2 = f.Data.scripted
    d.Window.spacebar3 = d.Window.spacebar2.render(d.Window.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Window.spacebar4 = d.Window.spacebar3.get_rect()
    d.Window.spacebar4.bottomleft = di.Data.left_col_2
    d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)'''
                 
