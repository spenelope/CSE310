
import time
from turtle import Screen
from player import Player
from item import ItemMovement
from player import ScoreLevel

class Main(Player, ItemMovement):

    screen = Screen()
    screen.setup(width=600, height=600) # Size of the display
    screen.tracer(0)

    player = Player()
    item_movement = ItemMovement()
    score_level = ScoreLevel()

    screen.listen()
    screen.onkey(player.go_up, "Up") # Binds actions to the keyrelease event. Arrow movement to 'Up'

    game_is_on = True # continue the game
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        item_movement.create_item() # create items
        item_movement.move_items() # manage the movement of the items
    
        for item in item_movement.all_items:  # Detect collision with item
            if item.distance(player) < 20: # distance between items
                game_is_on = False #game over
                score_level.game_over()

        if player.is_at_finish_line():    # Detect successful crossing
            player.go_to_start() #start the game
            item_movement.level_up() # the movement of the arrow is 'Up'
            score_level.increase_level() # increase the level number according to the time the element crosses the board

    screen.exitonclick() #This function is used to Go into mainloop until the mouse is clicked
