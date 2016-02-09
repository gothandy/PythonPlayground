class Base(object):

    def __init__(self, thing):

        self.thing = thing

    def Print(self):
        print(self.thing)

class Double(Base):

    def __init__(self, thing):
        Base.__init__(self, thing * 2)

b = Double('Hello World ')

b.Print()