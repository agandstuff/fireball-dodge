class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            _keyboard_service (KeyboardService): An instance of KeyboardService.
            _video_service (VideoService): An instance of VideoService.
            _total_lives (int): Initial value of the total lives available.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._total_lives = 5
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop. Game ends when the user closes the window or if all lives are lost

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            if self._total_lives > 0:
                self._get_inputs(cast)
                self._do_updates(cast)
                self._do_outputs(cast)
            else:
                self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with fireballs.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        fireballs = cast.get_actors("fireballs")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for fireball in fireballs:
            fireball.move_next(max_x, max_y)
            if player.get_position().equals(fireball.get_position()):
                cast.remove_actor('fireballs', fireball)
                self._total_lives -= fireball.get_life()

        banner.set_text('Lives: ' + str(self._total_lives)) 
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()