#!/Users/fljalufka/anaconda3/bin/python
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler



def main() -> None:
    screen_width = 80
    screen_height = 50

    # create the player position variables
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # read in the font that we want the game to use from the .png
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

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
            #tell the console where to print the @ symbol
            root_console.print(x=player_x, y=player_y, string="@")
            # updates the screen with what it has been told to display
            context.present(root_console)

            root_console.clear()
            # allows the game to be exited without crashing 
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
