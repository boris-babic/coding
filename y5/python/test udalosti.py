import tkinter, random, time
screenwidth, screenheight = 800,800
canvas = tkinter.Canvas(width = screenwidth, height = screenheight)
canvas.pack()


data = []
'''
with open('geografia.txt', encoding='utf-8') as file:
    for row in file:
        data.append(row.strip())

data.append(('Hlavne mesto haiti', 'Port au Prince'))
data.append(('Hlavne mesto kanady', 'Ottawa')) 
questions = []
for i in range(0,len(data)-1, 2):
    questions.append((data[i], data[i+1]))
'''
questions = []
questions.append(('Hlavne mesto haiti', 'Port au Prince'))
questions.append(('Hlavne mesto kanady', 'Ottawa'))
questions.append(('hlavne mesto slovenska', 'bratislava'))
def get_color(text):
    color_list = []
    for i in text:
        color_list.append(f'#{random.randrange(125, 256):02x}{random.randrange(125, 256):02x}{random.randrange(125, 256):02x}')
    return color_list   

def display_odpoved(text, color_list):
    canvas.delete('odpoved')
    a = 50
    x = screenwidth/2 - (len(text)/2*a)
    y = screenheight/2
    for i in range(len(text)):
        if text[i] != ' ':
            canvas.create_rectangle(x-a/2, y-a/2, x+a/2, y+a/2, fill=color_list[i], tag = 'odpoved')
            if text[i] != '*':
                canvas.create_text(x, y, text = text[i], font='Arial 20', tag = 'odpoved')
        x += a+5

def keypressed(event):
    global displayed, text
    for i in range(len(text)):
        if event.char == text[i]:
            displayed = displayed[:i] + text[i] + displayed[i+1:]
            
def get_displayed(text):
    displayed = ''
    for char in text:
        if char != ' ':
            displayed += '*'
        else:
            displayed += ' '
    return displayed

def scoreboard(length, time):
    canvas.delete('scoreboard')
    canvas.create_text(195, 30, text = f'Pocet zostavajucich otazok: {length}', font = 'Arial 20',tag = 'scoreboard')
    canvas.create_text(120, 60, text = f'Ostavajuci cas: {time}', font = 'Arial 20',tag = 'scoreboard')


            
question, text = questions.pop(random.randrange(len(questions)))
displayed = get_displayed(text)
canvas.create_text(screenwidth/2, screenheight/2-100, text=question, font = 'Arial 20', tag = 'question')
color_list = get_color(text)
start_time = time.time()

def timer():
    global text, displayed, color_list, start_time
    display_odpoved(displayed, color_list)
    time_left = round(10-(time.time()-start_time))
    scoreboard(len(questions), time_left)
    if '*' not in displayed:
        canvas.create_text(screenwidth/2, screenheight/2-200, text='HOTOVO good job', font = 'Arial 30')
    elif len(questions) == 0 and time_left == 0:
        canvas.create_text(screenwidth/2, screenheight/2-200, text='No nestihol si', font = 'Arial 30')
    elif time_left == 0:
        time_left ==10
        canvas.delete('question')
        question, text = questions.pop(random.randrange(len(questions)))
        displayed = get_displayed(text)
        canvas.create_text(screenwidth/2, screenheight/2-100, text=question, font = 'Arial 20', tag = 'question')
        color_list = get_color(text)
        start_time = time.time()
        canvas.after(100, timer)
    #pridane zastavenie po vycerpani otazok
    else:
        canvas.after(100, timer)
    


timer()
canvas.bind_all('<Key>', keypressed)
canvas.mainloop()