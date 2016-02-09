class Go(object):
    
    def __init__(self, exits):
        self.exits = exits

    def Execute(self, state, words):

        location = state['location']
        exit = words[0]
        exits = self.exits[location]
        newLocation = exits[exit]

        state.update({'location': newLocation})
        
        return [newLocation]


