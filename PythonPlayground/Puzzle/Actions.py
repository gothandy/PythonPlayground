import Story

from Commands import *

story = Story.story

actions = [ Where(story),
            Look(story),
            Go(story),
            Consequences(story) ]