import random
with open('/workspaces/ShakeAndBake/Hangman/words.txt', 'r' )as f:
    words = f.readlines()

def print_hangman(wrong):
    if(wrong == 7):
        print("\n +--+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 6):
        print("\n +--+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n +--+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n +--+")
        print(" O  |")
        print(" |\ |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n +--+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n +--+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 1):
        print("\n +--+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

word = random.choice(words)[:-1]
allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses : 
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    print_hangman(allowed_errors)
    guess = input(f"Allowed errors left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done :
    print(f"You found the word! It was {word}!")
else:
    print(f"Game over! The word was {word}!")
    
