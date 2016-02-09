class Where(object):

    def __init__(self, places):
        self.places = places

    def Execute(self, state, words):
        return ['Where are you?', self.places[state['location']]]