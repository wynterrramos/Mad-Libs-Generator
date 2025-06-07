# Vacation Fun Mad Libs Generator
# Created by: Wynter Ramos
# Date: 07 JUN 2025

# Story template sourced from the Mad Libs "Vacation Fun" printable:
# https://www.madlibs.com/printables/

# This script was created for educational purposes to practice collecting user input,
# storing values in variables, and using string formatting to generate a custom story.
# It is designed to be accessible to users of all experience levels, with built-in guidance and examples.

# Description:
# A simple Python program that takes user input and generates a personalized Mad Libs
# story using basic string formatting and variable assignment.

# Greetings/introduction to generator

print("\nWelcome to the Vacation Fun Mad Libs Generator!\n")
print("You will be prompted to enter different adjectives, verbs and nouns to create your own vacation story.\n")

# User guide

print("Quick Guide:")
print("\nAn adjective is a word that describes something (e.g., shiny, loud,old)")
print("A noun is a person, place, or thing (e.g., dog, pizza, mountain)")
print("Plural nouns refer to more than one person, place, or thing (e.g., dogs, pizzas, mountains)")
print("Verbs ending in 'ing' are action words ending in 'ing' (e.g., running, swimming, reading)\n")

print("Let's get started!\n")

# Collect user input for the Mad Libs story

name = input("Enter your name: ")
adjective1 = input("Enter an adjective (e.g., smelly, bright): ")
adjective2 = input("Enter an adjective: ")
noun1 = input("Enter a noun (e.g., dog, pizza): ")
noun2 = input("Enter a noun: ")
plural_noun1 = input("Enter a plural noun (e.g., apples, cars): ")
game = input("Enter a game (e.g., Monopoly, tag, Minecraft): ")
plural_noun2 = input("Enter a plural noun: ")
ing_verb1 = input("Enter a verb ending in 'ing'(e.g., dancing, talking): ")
ing_verb2 = input("Enter a verb ending in 'ing': ")
plural_noun3 = input ("Enter a plural noun: ")
ing_verb3 = input("Enter a verb ending in 'ing': ")
noun3 = input("Enter a noun: ")
plant = input("Enter a plant (e.g., cactus, rose): ")
body_part = input("Enter a part of the body (e.g., elbow, nose): ")
place = input("Enter a place (e.g., beach, zoo): ")
ing_verb4 = input("Enter a verb ending in 'ing': ")
adjective3 = input("Enter an adjective: ")
number = input("Enter a number (e.g., 7, 42): ")
plural_noun4 = input ("Enter a plural noun: ")

# User input collected

print("\nThanks for your answers! Let’s see what kind of story you’ve created: \n")

# Show the title of the story with user's name

print("Vacations, written by: " + name )

# Display completed story using input from user

print("\nA vacation is when you take a trip to some " + adjective1 + " place with your " + adjective2 + " family.")
print("Usually you go to some place that is near a/an " + noun1 + " or up on a/an " + noun2 + ".")
print("A good vacation place is one where you can ride " + plural_noun1 + " or play " + game + " or go hunting for " + plural_noun2 + ".")
print("I like to spend my time " + ing_verb1 + " or " + ing_verb2 + ". When my parents go on vacation, they spend their time eating three")
print(plural_noun3 + " a day, and they play golf, and mothers sit around " + ing_verb3 + ". Last summer, my little brother fell in a/an " + noun3)
print("and got poison " + plant + " all over his " + body_part + ". My family is going to go to (the) " + place + ", and I will practice")
print(ing_verb4 + ". Parents need vacations more than kids because parents are always very " + adjective3 + " and because they have to work " + number)
print("hours every day all year making enough " + plural_noun4 + " to pay for the vacation.\n")

# End message

print("The end!\n")


