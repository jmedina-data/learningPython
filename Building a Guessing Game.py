
# variables
secret_word = "giraffe"
guess = ""
# how many times the user guessed the word
guess_count = 0
# number of tries user has
guess_limit = 3
# weather or not the user has guesses left
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
# first check to see if the user has guesses left. if they do run it.
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        # if True no more guess left
        out_of_guesses = True

# ran out of guesses
if out_of_guesses:
    print("Out of guesses, You Lost!")
# if not then they win
else:
    print("You win!")