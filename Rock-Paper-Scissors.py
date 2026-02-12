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
random_list = ["rock","paper","scissors"]
computer_turn = random.choice(random_list)
user_choice = input("What do you choose. Type 0 for Rock, 1 for Scissors and 2 for Paper: ")



user_turn = ""
user_choice = int(user_choice)
if user_choice == 0:
    user_turn = "rock"
    print("You Choose")
    print(rock)
elif user_choice == 1:
    user_turn = "scissors"
    print("You Choose")
    print(scissors)
elif user_choice == 2:
    user_turn = "paper"
    print("You Choose")
    print(paper)
else:
    print("you selected wrong input. Please Start Over Again")



if computer_turn == "rock":
    print("Computer Chose")
    print(rock)
elif computer_turn == "paper":
    print("Computer Chose")
    print(paper)
else:
    print("Computer Chose")
    print(scissors)


if user_turn == computer_turn:
    print("Draw")
elif user_turn == "rock" and computer_turn == "scissors":
    print("You Win")
elif user_turn == "rock" and computer_turn == "paper":
    print("You Lose")
elif user_turn == "scissors" and computer_turn == "rock":
    print("You Lose")
elif user_turn == "scissors" and computer_turn == "paper":
    print("You Win")
elif user_turn == "paper" and computer_turn == "scissors":
    print("You Lose")
elif user_turn == "paper" and computer_turn == "rock":
    print("You Win")
