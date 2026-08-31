import random

'''
1 = Stone
2 = paper
3= scsissor

'''
dict = {"s": 1, "p": 2, "ss": 3}
reverse_dict = {1: "stone", 2: "paper", 3: "Scissor"}

while True:
    player = input("Enter your choice: ")
    if player == "Stop" or  player == "stop":
        print ("Game is stopped")
        break
    
    computer = random.choice([1,2,3])
    play = dict[player]

    print(f"you choose {reverse_dict[play]}\n computer choose {reverse_dict[computer]}")

    if (computer == play):
        print("It's  a draw")

    elif(computer == 1 and play == 2):
        print("You won!")

    elif(computer == 2 and play == 3):
        print("You win!")

    elif(computer == 3 and play == 1):
        print("You win!")

    elif(play == 1 and computer == 2):
        print("Computer won!")

    elif(play == 2  and computer == 3):
        print("computer won!")

    elif(play == 3 and computer == 1):
        print("computer won!")

    else:
        print("Somehing went wrong")
    

