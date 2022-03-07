
from turtle import Turtle
import random

COLORS = ["green", "blue", "orange", "yellow", "purple", "red"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class ItemMovement:

    def __init__(self):
        self.all_items = []
        self.item_speed = STARTING_MOVE_DISTANCE #Define the distance as constant

    def create_item(self):
        random_chance = random.randint(1, 6) #number of randoms items from 1-6
        if random_chance == 1:
            new_item = Turtle("circle") #Creates and returns a new turtle object
            new_item.shapesize(stretch_wid=1, stretch_len=1) #item size
            new_item.penup()
            new_item.color(random.choice(COLORS)) #Chose the color of the item in movement 
            random_y = random.randint(-250, 250)
            new_item.goto(300, random_y) #set the posotion 'y'
            self.all_items.append(new_item) # add item

    def move_items(self):
        for item in self.all_items:
            item.backward(self.item_speed)

    def level_up(self):
        self.item_speed += MOVE_INCREMENT
