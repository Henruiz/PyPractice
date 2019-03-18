import random

guesses = []

number_to_be_guessed = random.randint(1,99)

player = int(input("Guess a number between 1-99: "))
guesses.append(player)

while player != number_to_be_guessed:
    if player > number_to_be_guessed:
        print("Too High brotha! ")
    else:
        print ("Too Low brotha! ")

    player = int(input("Guess again! "))
    guesses.append(player)
else:
    print("You have guessed right! Good Job!")
    print("It took you %i guesses. " % len(guesses))
    print("These were your guesses: ")
    print(guesses)
    print("Thanks for playing! ")