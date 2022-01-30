from multiprocessing.connection import wait
import random
import time
from turtle import delay

# this funtion scrambles a word
def scramble_word(word):
    scramble = []

    for l in word:
        flip = random.choice([True, False])
        if (flip == True):
            scramble = [l] + scramble
        else:
            scramble = scramble + [l]

    puzzle = "".join(scramble)

    if (puzzle == word):
        puzzle = scramble_word(word)

    return puzzle


#print(word, " ---> ", scramble_word (word))

#this is the collection of words
word_bank = ["death", "giraffe", "chaotic", "dolphin", "banana", "elephant", "mango", 
    "monkey", "phone", "booth", "grapevine", "thunder", "goatee", "beanbag", "townhouse", 
    "canal", "marshland", "stairs", "caveman", "jokes", "comics", "anime", "pantheon", 
    "rosebush","cacti", "octopi", "sunset","quarterback","stargazer", "bubbles", "snowbank",
    "windmill", "hydroplane", "graphite", "philosphy", "musical", "genre", "whiteboard",
    "living", "balance", "heartbeat", "inferno", "squall", "alchemy", "transformation",
    "award", "performer", "stadium", "durable", "oasis", "character", "creative", "warrior",
    "chef", "protest", "against", "public", "infer", "problematic", "moral", "ashes", "bones",
    "vultures", "wolves", "moon", "howl", "psychology", "therapy", "miracle", "shield", "sword",
    "fight", "windowsill", "slowburn", "dabble", "quick", "interesting", "pajamas", "paddleboat",
    "under", "zero", "nothing", "journal", "multiple", "twins", "costumes", "matching", "light",
    "fire", "frenzy", "dog", "wolf", "waves", "airship", "sleek", "command", "games", "secret", 
    "message", "hidden", "book", "submarine", "sandwich", "fast", "food","swift", "red", "teardrops",
    "primadonna", "bubblegum", "satisfied", "heartstrings", "cream", "control", "freak", "dreamer",
    "impossible", "improbable", "mixed", "flying", "balloon", "lily", "animated", "heartbreaking", 
    "hellebore", "botany", "biology", "downfall", "opposites", "atract", "magnets", "meme", "structure",
    "society", "gossip", "papers", "romantic", "letters", "decayed", "becoming", "poetic", "biography",
    "double", "sleepovers", "fried", "baked", "icicles", "stabber", "wounds", "telltale", "ravens",
    "refine", "moor", "room", "manor", "classic", "harp", "lute", "coloums", "compass", "atlas", "map"
    "cartography", "mapmaker", "hymn", "tune", "fangs", "king", "angels", "royalty", "brave", "fold",
    "reverb", "vibes", "low", "darling", "dearest", "sweet", "sour", "good", "brutal", "traitor", "happier"
    "without", "influence", "scared", "remember", "marigolds", "roses", "editor", "author", "reader", "motorcycle"
    "accidents", "exist", "wrecking", "football", "nation", "marathon", "historical", "beautiful", "perfect", "genius"]

#this is the welcome screen code
def welcome():
    print("Welcome to Word Scrambler.")
    print("We have a library of %d words." % len(word_bank))
    print ("If you're ever tired of unscrambling, just hit enter and the code will end.")
    print("Copyright 2022 Marina Joseph.")
    print("Enjoy unscrambling!")

def score_print():
    print("You got %d right out of %d" %(correct, questions))


#this is the actual code that appears
welcome()

correct=0
questions=0

while (True):
    word = random.choice(word_bank)
    print("The clue is '%s'"% scramble_word(word))
    guess = input("Answer: ")

    if (guess == ""):
        score_print()
        time.sleep(3)
        break

    if (guess == word) :
        print("You're correct!")
        correct=correct + 1
        questions= questions + 1
    else:
        print("Sorry, the correct answer is '%s'"% word)
        questions = questions + 1
