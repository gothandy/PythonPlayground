from treedict import TreeDict

class Consequences(object):
    
    def __init__(self, story):
        self.consequences = story['consequences']

    def Execute(self, command, state):

        stateTree = TreeDict(state)

        for consequence in self.consequences:

            if consequence[0](stateTree):

                state.update({'dead': True})
                return [consequence[1]]


