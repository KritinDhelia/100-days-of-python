import random
print("This is a guessing game. you have to enter a small no and a big no. the computer will randomly pick a number in the middle and you have to guess the number. if you guess wrong you will be given clues to find the number")
small = int(input("enter small no. "))
big = int(input("enter big no. "))
num = random.randint(small, big)
guess = small-3
while(guess != num):
    guess = int(input("enter no. "))
    if guess == num:
        print("you guessed correctly")
    elif guess > num:
        print("Your guess is too big")
    else:
        print("Your guess is too small")