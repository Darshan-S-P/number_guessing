import random 

top_of_range = input ("Type a Upper range number:  ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a grater then then zero next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess:  "  )
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("Your answer is greater then random guess")
        else:
            print("Your answer is smaller then random guess")

print("You got it in", guesses, "guesses")
