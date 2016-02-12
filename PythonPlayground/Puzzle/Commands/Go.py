class Go(object):
    
    def __init__(self, story):
        self.exits = story['exits']

    def Execute(self, command, state):

        words = command.split()

        if words[0] != 'go':
            return None

        location = state['location']
        exit = words[1]
        exits = self.exits[location]
        newLocation = exits[exit]

        state.update({'location': newLocation})
        
        return [newLocation]


