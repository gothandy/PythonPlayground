class Where(object):

    def __init__(self, story):
        self.places = story['places']

    def Execute(self, command, state):

        words = command.split()

        if words[0] != 'look':
            return None

        location = state['location']

        return [self.places[location]]