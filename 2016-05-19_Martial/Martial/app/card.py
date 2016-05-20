class Card(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def paint(self,window):
        width = 15
        height = max(self.description.__len__() // (width - 4) + 5, 6)
        box = window.getBox(height, width)

        box.hsplit(2)
        
        box.put(1,2,self.name)
        
        box.putWrap(3,2,height-1,width-4,self.description)
        
