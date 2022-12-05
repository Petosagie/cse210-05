from game.casting.actor import Actor

class GameOverMessage(Actor):
    """Show the Game Over message.
    """

    def __init__(self):
        super().__init__()
        self._text = "Game Over"


    def get_text(self):
        """Obtain the class message
        """
        return self._text