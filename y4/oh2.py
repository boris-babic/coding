'''
import tkinter
canvas= tkinter.Canvas(width=1000, height= 500)
canvas.pack()
'''
#1
def temperatures(input):
    text = input.lower()
    text = text.strip()
    value = float(text[:-1])
    if 'f' in text:
        print(text.upper(), '=', round((value-32)/1.8, 1), 'C')
    elif 'c' in text:
        print(text.upper(), '=', round(value*1.8+32, 1), 'F')
    else:
        print('toto neviem prekonvertovat')
'''

#2

def iteration():
    i=0
    iterate = []
    objects = [chr(111), chr(98)]
    for char in [chr(115), chr(105), chr(114)]:
        iterate.append(char)
    while len(iterate)<5:
        iterate.append(objects[i])
        i+=1
    iterate.reverse()
    return iterate

def get_dictionary(input1, input2):
    dictionary = {}
    list = input2
    q = 0
    while len(input1)>len(list):
        q+=1
        list.append(q)
    for i in range(len(input1)):
        dictionary[list[i]] = input1[i]
    return dictionary

def squares(size, string):
    author= 'made by boris'
    x=100
    y=100
    counter = get_dictionary(string.split(), iteration())
    for k, v in counter.items():
        if k in iteration():
            canvas.create_text(x+ size/2, y+size/2, text=k, font='Arial 20')
        canvas.create_rectangle(x, y, x+size, y+size, fill= v)
        x+= size+10
squares(80, 'red blue green yellow orange navy red blue green')


canvas.mainloop()
'''
import tkinter
c= tkinter.Canvas(height=600, width=700)
c.pack()

def stvorce(v, farby ):
    x=10
    y=100
    while ' ' in farby:
        x+= 2*v+10
        vypln= farby[:farby.find(' ')]
        farby= farby[farby.find(' ')+1:]
        c.create_rectangle(x+v, y+v, x-v, y-v, fill= vypln)
    x+= 2*v+10
    c.create_rectangle(x+v, y+v, x-v, y-v, fill= farby)


stvorce(40, 'red blue purple red gold purple')
c.mainloop()