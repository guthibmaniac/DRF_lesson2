# def name():
#     x = int(input("x: "))
#     y = int(input("y: "))
#     z = input("z: ")
#     if z == "+":
#         print(x + y)
#     elif z == "-":
#         print(x - y)
#     elif z == "*":
#         print(x * y)
#     elif z == "/":
#         print(x / y)

# name()
import random
random2 = random.choice(['rock', 'scissors', 'paper'])
def game():
    user = input("rps:")
    if user == random2:
        print("Computer:", random2)
        print("Draw")
    elif (user == "rock" and random2 == "scissors") or (user == "scissors" and random2 == "paper") or (user == "paper" and random2 == "rock"):
        print("Computer:", random2)
        print("You win")
    else:
        print("Computer:", random2)
        print("You lose")
game()