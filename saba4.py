#Program 1-Build a Cars Deck
import random

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
face_cards = ["Jack", "Queen", "King", "Ace"]
number_cards = list(range(2, 11))  

def draw():
    card = random.choice(face_cards + number_cards)
    suit = random.choice(suits)
    return (str(card), "of", suit)

print(draw())


#Program 2-Draw Five Cards
for i in range(5):
    print(draw())

#Program 3-Explore a string Value
filename = "Darius-13-100m-Fly.txt"

print(filename.upper())
print(filename.lower())
print(len(filename))

#Program 4-Split a string
sentence = "So long, and thanks for all the fish."

print(sentence.split())
print(sentence.split(", "))

#program 5-Extract Data into Variables
filename = "Darius-13-100m-Fly.txt"

name_only = filename.replace(".txt", "")
pieces = name_only.split("-")

swimmer_name = pieces[0]
age_group = pieces[1]
distance = pieces[2]
stroke = pieces[3]

print(swimmer_name, age_group, distance, stroke)

