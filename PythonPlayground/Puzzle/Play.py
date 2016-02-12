import Actions

from Engine import Engine

state = { 'location': 'hab', 'objects': { 'suit': 100 }}

engine = Engine(Actions.story, Actions.actions, state)

while True:

    command = input(':')

    for line in engine.Act(command):
        print(line)

    if 'dead' in state and state['dead'] == True:
        break
    