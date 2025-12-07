#Python_number_guessing_game

import random


friend_name = input("Please enter your good name: ").lower()

print("Please enter 'hi' to start the game.")
user_input = input("Enter input: ")

if user_input.lower() == "hi":
    print(f"Hello, {friend_name}. Welcome back to guessing world, specially designed for you by Mr. ArunRaj.")
    print("Select your difficulty level(easy/medium/hard): ")
    user_input2 = input().lower()
    if user_input2 == "easy":
        print("Great! That you selected an easy level.\nI am thinking of a number between 1 and 20.\nTry to guess it.")


    secret_number = random.randint(1, 20)

    while True:
        guess = input(f"take a guess: ")
        if not guess.isdigit():
            print(f"{friend_name}, numbers only. Do not try to fool me")
        guess = int(guess)

        if guess == secret_number:
            print(f"oh {friend_name} Great! That's exactly correct answer. Genius level of IQ")
            break
        elif guess < secret_number:
            print(f"Too Low {friend_name}, Try again: ")
        else:
            print(f"Too High {friend_name}, Try again: ")
else:
    print("You did not type hi. Restart and greet me first.")