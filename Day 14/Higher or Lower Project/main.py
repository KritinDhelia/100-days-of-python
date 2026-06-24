import random
from game_data import data

correct = True
score = 0
a=random.randint(0,len(data)-1)
b=random.randint(0,len(data)-1)
choice = ''
winner=''
while(correct):
    print(f"compare A: name: {data[a]['name']} follower_count: {data[a]['follower_count']} description: {data[a]['description']} : {data[a]['country']}")

    while(a==b):
        b = random.randint(0, len(data) - 1)

    print(f"to B: name: {data[b]['name']} description: {data[b]['description']} : {data[b]['country']}")
    choice=input("Enter your choice as to who has more insta followers, press a or b in lower case: ")
    if (choice=='a'and data[a]['follower_count']>data[b]['follower_count']):
        print("You guessed correctly")
        score+=1
        winner = a
    elif(choice=='b'and data[b]['follower_count']>data[a]['follower_count']):
        print("You guessed correctly")
        score+=1
        winner = b
    else:
        print("You guessed incorrectly")
        print(f"your score is {score}")
        correct = False
    a=winner
    b=random.randint(0, len(data) - 1)