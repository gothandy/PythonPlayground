from Commands import *

story = { 
    'places': { 'hab': 'You are in the hab.',
               'outside': 'You are outside the hab.'},
    'exits': { 'hab': { 'airlock': 'outside' }},
    'objects': { 'hab': ['Flight Suit'] }
    }

state = { 'location': 'hab' }

commands = { 'look': Look(story['objects']),
             'where': Where(story['places']),
             'go': Go(story['exits'])}

tests = ['look', 'where', 'go airlock', 'where', 'look']

for test in tests:
    words = test.split()
    lines = []

    if (len(words) == 1):
        lines = commands[words[0]].Execute(state, [])
    else:
        lines = commands[words[0]].Execute(state, words[1:])

    print(test)
    for line in lines:
        print(line)