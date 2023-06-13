import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images_list = [rock,paper,scissors]
input_list = ["Rock" , "Paper" , "Scissor"]
exit_flag = True
while exit_flag:
    user_input = int(input("Enter 0 for Rock , 1 for Paper and 2 for scissor \n"))
    computer_input=0
    if user_input in range (0,3):
        print(f" you have entered - {input_list[user_input]}   {images_list[user_input]}")
        computer_input = random.randint(0,2)
        print(f" Computer have entered - {input_list[computer_input]}   {images_list[computer_input]}")
        ## check the Posibbilities of user wins2

        if (user_input == 0 and computer_input ==2 ) or (user_input == 2 and computer_input ==1) or (user_input == 1 and computer_input ==0):
            print("YOU HAVE WON  -- CHEERS")
        elif (computer_input == 0 and user_input ==2 ) or (computer_input == 2 and user_input ==1) or (computer_input == 1 and user_input ==0):
            print("YOU HAVE LOST  -- BETTER LUCK NEXT TIME ....")
        elif computer_input == user_input:
            print("IT'S DRAW , PLAY AGAIN ....")
    elif user_input == 3 :
        exit_flag=False
    else:
        print("you have entered the Incorrect Value")
