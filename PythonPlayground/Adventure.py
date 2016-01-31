import json

with open('story.json', encoding='utf-8-sig') as storyFile: 

    story = json.load(storyFile)

options = story['start']
  
while True:

    answer = input(': ').lower()

    if answer == 'exit':
        break

    elif answer == 'help':
        print('Try', ', '.join(iter(options)), 'or exit.')

    elif answer not in options:
        print('You can\'t', answer)

    else:
        print(options[answer]['text']) 

        if 'exit' in options[answer]:
            break

        if 'next' in options[answer]:
            options = story[options[answer]['next']]
