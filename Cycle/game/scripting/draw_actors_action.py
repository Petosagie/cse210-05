from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """This Class will move the body of the Snake
    also will override the method execute from Action
    Class.
    """
    def __init__(self) -> None:
        super().__init__()


    def execute(self, cast, script):
        all_actors = cast.get_all_actors()
        for actor in all_actors:
            actor.move_next()

