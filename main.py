# TASK 1 :Guess the number
""" The computer randomly selects a number within a range, and the player has to guess it
"""
import random 
n = random.randint(1, 50)  #choosing random number between range 1 to 50
print(f"Random number is: {n}")
count = 0
print("Guess the number between 1 and 50")

#Use of while loop and storing values in variables g, n
while True:
    g = int(input("Enter your guess:"))
    count +=1

    if g > n:
        print("Guessed number is greater than random number")
    if g < n:
        print("Guessed number is less than random number")
    if g==n:
        print(f"Guessed number is equal to random number in {count} counts")
        break

#TASK 2 : WORD SCRAMBLE
import random

words = ['python', 'javascript', 'java', 'automation','pytest','guvi','selenium']
# Picks a random word from words list
random_word = random.choice(words) 
print(random_word) 
#convert random_word from string to list, segregating alphabets
scrambled_word = list(random_word)
print(scrambled_word)
random.shuffle(scrambled_word)  # Shuffles alphabets in place
unscrambled_word = ''.join(scrambled_word)
print(f"Unscramble: {unscrambled_word}")
#using while loop
count = 0
while True:
    count += 1 
    Guess_word = input("Enter your guess word from words:")
    if random_word != Guess_word:
        print("Try again")
        
    else:
        print("Got the desired word")
        break
   
