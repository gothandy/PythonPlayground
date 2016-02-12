import unittest
import Actions

from Engine import Engine

def printAll(state, commands):

    engine = Engine(Actions.story, Actions.actions, state)

    for action in commands:
        for line in engine.Act(action):
            print(line)

class Test_Basic(unittest.TestCase):

    def test_nosuit(self):

        printAll({ 'location': 'hab' },
                 ['look', 'go airlock'])

    def test_suitoutandback(self):
       
        printAll({ 'location': 'hab', 'objects': 'suit'},  
                 ['look', 'go airlock', 'look', 'go airlock', 'look'])    


if __name__ == '__main__':
    unittest.main()
