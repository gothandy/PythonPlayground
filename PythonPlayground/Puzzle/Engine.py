class Engine(object):

    def __init__(self, story, actions, state):
        self.story = story
        self.state = state
        self.actions = actions

    def Act(self, command):

        match = False

        for action in self.actions:
            output = action.Execute(command, self.state)

            if output != None:
                match = True
                yield from output

        if not match:
            yield('I don\'t understand')
