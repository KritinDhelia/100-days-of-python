import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while(choice == 'y'):
    winner = "none"
    dealersum = 0
    usersum = 0
    user = [random.choice(cards),random.choice(cards)]
    dealer = [random.choice(cards),random.choice(cards)]
    usersum+=user[0]+user[1]
    dealersum+=dealer[0]+dealer[1]
    print(f"your cards are {user}")
    print(f"dealer's 1st card is {dealer[0]}")
    if(dealersum == 21):
        winner = "dealer wins!"
        print(winner)
    elif(usersum == 21):
        winner = "you win!"
        print(winner)
    else:
        newcard=input("Do you want another card? Type 'y' or 'n': ")
        while(newcard=='y'):
            user.append(random.choice(cards))
            print(f"your cards are {user}")
            usersum +=user[len(user)-1]
            if(usersum > 21):
                if(11 in user):
                    usersum -=10
                else:
                    winner = "dealer wins!"
                    print(winner)
                    break
            newcard = input("Do you want another card? Type 'y' or 'n': ")
        if(winner=="none"):
            while(dealersum<16):
                dealer.append(random.choice(cards))
                dealersum += dealer[len(dealer) - 1]
                if (dealersum > 21):
                    if (11 in dealer):
                        dealersum -= 10
                    else:
                        winner = "you win!"
                        print(winner)
                        break
    if(winner=="none"):
        if(dealersum>usersum):
            print("dealer wins!")
        elif(usersum>dealersum):
            print("you win!")
        else:
            print("draw")
    print(user)
    print(dealer)
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")