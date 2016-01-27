wellBottom = {
    'look': {'print': 'You can see a bucket above' }
    }

lightOn = {
    'door': {'print': 'You open the door and are in the bottom of a well', 'answers': wellBottom}
    }

start = {
    'light': {'print': 'You can see a door', 'answers': lightOn }, 
    'eat': {'print': 'You have nothing to eat'}
    }

answers = start

while True:

    answer = input(': ').lower()

    if answer == 'exit':
        break
    elif answer == 'help':
        for key in iter(answers):
            print(key)
    elif answer not in answers:
        print("You can't", answer)
    else:
        print(answers[answer]['print']) 

        if 'answers' in answers[answer]:
            answers = answers[answer]['answers']
