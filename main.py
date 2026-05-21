import random


# Mtg colors as variables for the random function
Black = "Black"
Red = "Red"
Blue = "Blue"
Green = "Green"
White = "White"


# the list of variables to select from
mtg_colors = [Black, Blue, Red, White, Green]


# randomly select and show one of the colors
selected = random.choice(mtg_colors)


print(selected)



