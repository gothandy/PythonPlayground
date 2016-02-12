story = { 
    'places': {
        'hab': 'You are in the hab.',
        'outside': 'You are outside the hab.'
        },
    'exits': {
        'hab': { 'airlock': 'outside' },
        'outside': { 'airlock': 'hab' }
        },
    'objects': {
        'hab': ['Flight Suit'],
        'outside': ['rover']
        },
    'consequences': [
        (lambda state: state['objects', 'suit'] is not None and state['location'] == 'outside', 'You really need a suit outside.'),
        (lambda state: state.getdefault('objects', 'suit', default=0) == 0 and state['location'] == 'outside', 'You ran out of oxygen.')
        ]
    }
