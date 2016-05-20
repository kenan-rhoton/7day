class Box(object):

    def __init__(self, window, height, width) :
        self.width = width
        self.height = height
        self.win = window.derwin(height, width, 0, 0)
        self.win.border()

    def hsplit(self, line):
        self.win.hline(line,1,"-",self.width - 2)

    def put(self, y, x, text):
        self.win.addstr(y, x, text)

    def putWrap(self, y, x, height, width, text):

        line = y
        desc = text
        for i in range(0,height - y):
            if desc.__len__() > (width):
                self.win.addnstr(line, x, desc, width)
                desc = desc[width:]
            else:
                self.win.addstr(line,x,desc)
                break

            line+=1
