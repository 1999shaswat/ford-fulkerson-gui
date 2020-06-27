from p5 import *

width = 800
height = 600
mode = 'p'
vertex = []
edge = None
# mouse_lock=0


class Spot:
    def __init__(self, i, j, index):
        self.i = i
        self.j = j
        self.index = index
        self.col = Color(random_uniform(50, 150), random_uniform(
            50, 150), random_uniform(50, 150))

    def show(self):
        fill(self.col)
        no_stroke()
        circle((self.i, self.j), 20, CENTER)

    def select(self):
        fill(0)
        no_stroke()
        circle((self.i, self.j), 20, CENTER)

    def __str__(self):
        return f'{self.i},{self.j}{self.index}'


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


def draw():

    for spot in vertex:
        spot.show()
    if mode=='e':
        if start!=None:
            start.select()
    if edge!=None:
        for i in range(len(edge)):
            for j in range(len(edge)):
                if edge[i][j]>0:
                    # TODO: edge is drawn here. change colors
                    stroke(Color(0,255,153))
                    stroke_weight(4)
                    line((vertex[i].i,vertex[i].j),(vertex[j].i,vertex[j].j))
    print(len(vertex))


start = None
end = None


def mouse_pressed():
    global start, end
    if mode == 'e':
        start = findclosest()
        


def mouse_released():
    global start, end, edge
    if mode == 'e':
        end = findclosest()
        edge[start.index][end.index]=1
        start, end = None, None


def mouse_clicked():
    if mode == 'p':
        ind = len(vertex)
        vertex.append(Spot(mouse_x, mouse_y, ind))


def key_pressed():
    global mode, msg, edge
    if mode != 'r':
        mode = str(key)
        if mode == 'p':
            msg = "points"
        elif mode == 'e':
            edge = [[0 for x in vertex] for y in vertex]
            msg = "edges"
        elif mode == 's':
            msg = "source"
        elif mode == 't':
            msg = "Target"
        elif mode == 'r':
            msg = "Running..."


if __name__ == '__main__':
    run()
