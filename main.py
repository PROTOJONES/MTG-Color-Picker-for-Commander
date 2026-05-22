import random




# Color variables
Black = "Black"
Red = "Red"
Blue = "Blue"
Green = "Green"
White = "White"



# User input to choose amount of colors
choice = int(input("How many colors would you like your commander to be? Enter a Number 1-3:  "))
if not 1 <= choice <= 3:
    print("INVALID PLEASE SELECT A NUMBER BETWEEN 1 AND 3")




else:



    # Mono Colors
    mono_colors = ["Mono Red",
                   "Mono Green",
                   "Mono Blue",
                   "Mono White",
                   "Mono Black"
    ]

# If user chooses 2 Colors
two_colors = [
    "Gruul (Green + Red)",
    "Rakdos (Red + Black)",
    "Izzet (Blue + Red)",
    "Selesneya (White + Green)",
    "Golgari (Green + Black)",
    "Boros (White + Red)",
    "Orzhov (Black + White)",
    "Dimir (Black + Blue)",
    "Simic (Green + Blue)"
]


# If user chooses 3 Colors
three_colors = [
    "Abzan (White+ Green + Black)",
    "Bant (White + Blue + Green)",
    "Esper (White + Blue + Black)",
    "Grixis (Blue + Black + Red)",
    "Jeskai (White + Blue + Red)",
    "Jund (Black + Red + Green)",
    "Mardu (White + Black + Red)",
    "Naya (White + Red + Green)",
    "Sultai (Blue + Black + Green)",
    "Temur (Blue + Red + Green)"
]


if choice == 1:
    selected=random.choice(mono_colors)


elif choice == 2:
    selected=random.choice(two_colors)


elif choice == 3:
    selected=random.choice(three_colors)




print("Your commander colors are:")
print(selected)