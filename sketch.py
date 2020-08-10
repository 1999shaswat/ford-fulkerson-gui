from process import *

from p5 import *
from easygui import enterbox

width = 800
height = 600
mode = 'p'
vertex = []
edge = None
msg='Vertices'
src = None
sink = None
dic={}
max_flow=0

class Spot:
    def __init__(self, i, j, index):
        self.i = i
        self.j = j
        self.index = index
        self.col = Color(255, 0, 147)

    def show(self):
        fill(self.col)
        no_stroke()
        circle((self.i, self.j), 20, CENTER)

    def select(self):
        fill(Color(20, 99, 255))
        no_stroke()
        circle((self.i, self.j), 20, CENTER)

    def __str__(self):
        return f'{self.i},{self.j}{self.index}'


def textpos(a, b):
    (x1, y1) = a
    (x2, y2) = b
    mx, my = (x1+x2)/2, (y1+y2)/2
    m = -1.0/((y2-y1)/(x2-x1))
    ax, ay = 0, 0
    l = 40
    if m == 0:
        ax = mx+l
        ay = my
    elif m > 10**9:
        ax = mx
        ay = my+l
    else:
        dx = 1/sqrt(1+(m*m))
        dy = m*dx
        ax = mx+dx
        ay = my+dy
    return ax, ay


def findclosest():
    '''
    finds closest point to mouse and returns it
    '''
    m = 10**5
    i = 0
    for s in vertex:
        if dist((s.i, s.j), (mouse_x, mouse_y)) < m:
            i = s
            m = dist((s.i, s.j), (mouse_x, mouse_y))
    return i


def setup():
    size(width, height)
    f = create_font("Arial.ttf", 18)
    text_font(f)


def draw():
    global mode,dic,max_flow,msg
    background(50)


    if edge != None:
        for i in range(len(edge)):
            for j in range(len(edge)):
                if edge[i][j] > 0 or (mode in {'r','d'} and edge[j][i] > 0):
                    # TODO: edge is drawn here. change colors
                    stroke(Color(255, 0, 147))
                    stroke_weight(4)
                    line((vertex[i].i, vertex[i].j),
                         (vertex[j].i, vertex[j].j))
                    x, y = textpos(
                        (vertex[i].i, vertex[i].j), (vertex[j].i, vertex[j].j))
                    fill(Color(255, 0, 147))
                    no_stroke()
                    if mode not in {'r','d'}:
                        text(f'{edge[i][j]}', (x, y))
                    else:
                        if dic.get((i,j))!=None:
                            print(i,j)
                            text(f'{edge[j][i]}', (x, y))

    for spot in vertex:
        spot.show()
        if start != None:
            stroke(Color(255, 0, 147))
            stroke_weight(4)
            line((start.i, start.j), (mouse_x, mouse_y))
            start.select()
    
    print(edge)
    
    if mode == 'r':
        for i in range(len(edge)):
            for j in range(len(edge[0])):
                if edge[i][j]>0:
                    dic[(i,j)]=True
        max_flow = solution(edge, src.index, sink.index)
        print(max_flow)
        msg="Done"
        mode = 'd'
        no_loop()
    
    if mode=='d':
        fill(255)
        no_stroke()
        text(f'maximum flow:{max_flow}', (width-200, height-20))

    fill(255)
    no_stroke()
    text(f'mode:{msg}', (10, height-20))
    # if mode != 'r' or mode != 'd':

    # for spot in vertex:
    #     if mode == 'e':
    #         if start != None and spot == start:
    #             stroke(Color(255, 0, 147))
    #             stroke_weight(4)
    #             line((start.i, start.j), (mouse_x, mouse_y))
    #             start.select()
    #         else:
    #             spot.show()
    #     else:
    #         spot.show()


start = None
end = None


def mouse_pressed():
    global start, end
    if mode == 'e':
        start = findclosest()


def mouse_released():
    global start, end, edge, mode
    if mode == 'e':
        end = findclosest()
        # val=int(input())
        try:
            val = int(enterbox(msg="Edge capacity",
                               title="Edge", default='', strip=True))
        except ValueError:
            val = 0
        edge[start.index][end.index] = val
        # edge[end.index][start.index] = val
        start, end = None, None
        mode = 'e'


def mouse_clicked():
    global src, sink
    if mode == 'p':
        ind = len(vertex)
        vertex.append(Spot(mouse_x, mouse_y, ind))
    elif mode == 's':
        if src != None:
            src.col = Color(255, 0, 147)
        src = findclosest()
        src.col = Color(0, 255, 0)
    elif mode == 't':
        if sink != None:
            sink.col = Color(255, 0, 147)
        sink = findclosest()
        sink.col = Color(0, 0, 255)


def key_pressed():
    global mode, msg, edge, weight, letters
    if mode != 'r' and mode != 'd':
        # if mode == 'i':
        #     if key == "BACKSPACE":
        #         if len(letters) > 0:
        #             letters = letters[:-1]
        #     elif key == "ENTER":
        #         val = int(letters)
        #         letters = ""
        #         mode = 'e'
        #         return val
        #     else:
        #         letters = letters + str(key)

        mode = str(key)
        if mode == 'p':
            msg = "Vertices"
        elif mode == 'e':
            if edge == None:
                edge = [[0 for x in vertex] for y in vertex]
                msg = "Edges"
        elif mode == 's':
            msg = "Source"
        elif mode == 't':
            msg = "Target"
        elif mode == 'r':
            msg = "Running..."


if __name__ == '__main__':
    run()
