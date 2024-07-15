#!/Users/fljalufka/anaconda3/bin/python
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler



def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    # read in the font that we want the game to use from the .png
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # creates the screen with width and height set earlier
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        # creates the console the game draws to and sets it to the same size as the terminal
        root_console = tcod.Console(screen_width, screen_height, order="F")
        #create game loop
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)



if __name__ == "__main__":
    main()
