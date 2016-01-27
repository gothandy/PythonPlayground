story = {
    'wellBottom': {
        'look': {'text': 'You can see a bucket above' },
        'back': {'text': 'You go back through the door',
                 'next': 'lightOn'}
        },
    'lightOn': {
        'open': {'text': 'You open the door and are in the bottom of a well',
                 'next': 'wellBottom'}
        },
    'start': {
        'light': {'text': 'You can see a door',
                  'next': 'lightOn' }, 
        'eat': {'text': 'You have nothing to eat'}
        }
    }

answers = story['start']
  
while True:

    answer = input(': ').lower()

    if answer == 'exit':
        break

    elif answer == 'help':
        print('Try', ', '.join(iter(answers)))

    elif answer not in answers:
        print('You can\'t', answer)

    else:
        print(answers[answer]['text']) 

        if 'next' in answers[answer]:
            answers = story[answers[answer]['next']]
