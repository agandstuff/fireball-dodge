
import random

from constants import *

from game.casting.actor import Actor
from game.casting.fireball import Fireball
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    y = int(MAX_Y / 2)
    position = Point(45 + CELL_SIZE, y)

    player = Actor()
    player.set_text("O")
    player.set_font_size(FONT_SIZE + 15)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)
    
    # create the fireballs
    for n in range(DEFAULT_FIREBALLS):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 3)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        color = Color(255, 80, 0)

        
        fireball = Fireball()
        fireball.set_text("*=")
        fireball.set_color(color)
        fireball.set_font_size(FONT_SIZE + 10)
        fireball.set_position(position)
        fireball.set_velocity(Point(-15,0))
        cast.add_actor("fireballs", fireball)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()