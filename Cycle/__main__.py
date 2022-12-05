import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # Create both instances of the snakes or cycles
    player_one = Snake(Point(int(constants.MAX_X - 675), int(constants.MAX_Y / 2)))
    player_one.set_cycle_color(constants.RED)
    player_two = Snake(Point(int(constants.MAX_X - 225), int(constants.MAX_Y / 2)))
    player_two.set_cycle_color(constants.GREEN)

    # create the cast
    cast = Cast()
    cast.add_actor("player_one", player_one)
    cast.add_actor("player_two", player_two)
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()