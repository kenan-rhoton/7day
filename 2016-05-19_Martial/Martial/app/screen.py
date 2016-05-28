import curses
from app.box import Box

class Screen(object):

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.raw()
        curses.cbreak()

    def end(self):
        curses.nocbreak()
        curses.noraw()
        curses.echo()
        curses.endwin()
    
    def getBox(self, width, height):
        return Box(self.stdscr, width, height)

    def put(self, text):
        self.stdscr.addstr(0, 0, text)

    def dump(self):
        string = ""
        size = self.stdscr.getmaxyx()
        for y in range(0, size[0]):
            for x in range(0, size[1]):
                string+=self.stringify(self.stdscr.inch(y,x))
        return string

    def stringify(self, number):
        return chr(number & int('11111111',2))
