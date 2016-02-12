import Join

class Look(object):

    def __init__(self, story):
        self.objects = story['objects']

    def Execute(self, command, state):

        words = command.split()

        if words[0] != 'look':
            return None

        location = state['location']

        if location in self.objects:
            objects = self.objects[location]
            return [Join.Coordinating(objects)]
        else:
            return ['Nothing here.']

            