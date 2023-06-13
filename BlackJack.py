## This program will play Black jack with computer and users
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
computer_is_winner = False
user_is_winner = False
continue_to_play=True

user_has_ace = False
computer_has_ace=False

## Function to draw the cards
def draw_cards ():
    return random.choice(cards)

user_cards=[]
computer_cards=[]

## Draw first 2 cards
for i in range (2):
    user_cards.append(draw_cards())
    computer_cards.append(draw_cards())
## while loop to play the game until user want
while continue_to_play:
    print(f" user cards are {user_cards}")
    print(f" Computer cards are {computer_cards}")
    user_total =  sum(user_cards)
    computer_total =  sum(computer_cards)

    ## check for black jack
    if 11 in user_cards and 10 in user_cards and len(user_cards) ==2 :
        user_has_ace = True
        user_is_winner=True
    if sum(computer_cards) == 21 and len(computer_cards) == 2:
        computer_has_ace=True
        computer_is_winner=True
    # for item in computer_cards:
    #     if item == 11:
    #         computer_has_ace = True
    #         if user_total == 10:
    #             computer_is_winner=True
    #             break

    ## check if user has Ace and sum is greater than 21
    if user_total > 21 and user_has_ace == True:
        # user_total -= 10
        user_cards.remove(11)
        user_cards.insert(1)
        user_total =  sum(user_cards)
        if user_total > 21:
            computer_is_winner = True
            break
    if user_total <= 21:
        user_option=input("Do you want another card  'Y' for yes and 'N' for no")
        if user_option == 'N':
            while(computer_total < 17 ):
                computer_cards.append(draw_cards())
                computer_total = sum(computer_cards)
                print(f" Computer cards are {computer_cards}")
            if computer_total > 21:
                user_is_winner = True
            elif user_total > computer_total:
                user_is_winner = True
            elif computer_total > user_total:
                computer_is_winner=True
            continue_to_play=False
        else:
            user_cards.append(draw_cards())
    else:
        continue_to_play = False

if not user_is_winner  and not computer_is_winner:
    print("DRAW")
elif user_is_winner:
    print(f"User is Winner  total value is {user_total}")
else:
    print(f"Computer is Winner - total value is {computer_total}")










# print(f" user cards {user_cards}")
# print(f" computer cards {computer_cards}")




