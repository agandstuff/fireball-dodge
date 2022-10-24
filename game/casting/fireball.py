from game.casting.actor import Actor

class Fireball(Actor):
    """Objects which are randomly placed, and which have particular points depending on the fireball, and in which the player attempts to avoid.

    Attributes:
        super().__init__() = Attributes from the parent class (Actor).
        _life (int): Life value belonging to the Fireball.
    """

    def __init__(self):
        """ Constructs a new Fireball. """
        super().__init__()
        self._life = 1

    def get_life(self):
        """ Gets the fireball's life value.

            Returns:
            _life (int): The fireball's life value.
        """
        return self._life