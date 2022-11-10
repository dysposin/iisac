class Image(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        if self:
            if type(self[0]) != list:
                self = [self]
        self.width = len(self[0])
        self.height = len(self)
        self.origo = (0, 0)


    @property
    def size(self):
        return (self.width, self.height)
   
 
    def __str__(self):
        if self.height <= 1:
            return ''.join(str(v) for v in self)
        else:
            return '\n'.join([''.join(str(c) for c in row) for row in self])
