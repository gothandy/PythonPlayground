import Join

class Look(object):

    def __init__(self, objects):
        self.objects = objects

    def Execute(self, state, words):

        location = state['location']

        if location in self.objects:
            objects = self.objects[location]
            return [Join.Coordinating(objects)]
        else:
            return ['Nothing here.']

            