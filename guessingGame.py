import random
print("Number guessing game")
number = random.randint(1,9)
chances = 0 
print("Guess a number between 1 and 9 ")

while chances < 5:
    guess = int(input("Enter your guess"))

    if guess == number:
        print("Congrats you win!")
        break 

    elif guess < number:
        print("Your guess was too low, think of a number higher", guess)
    
    else:
        print("Your guess was too high, think of a number lower", guess)


chances += 1 

if not chances < 5:
    print("You lost, the number is", number)
