from pygame import *
import random

print("                                                               --------Welcome To The Game-------")
print("                                                               --------STONE PAPER SCISSOR--------")
def music_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    # while True:
    #     # a = input("type 'stop' when you done the task :")
    #     if a == stopper:
    #         mixer.music.stop()
    #         break

def game():
    attempt = 1
    your_points = 0
    computer_points = 0

    while attempt <= n:
        choose = ["r", "p", "s"]
        ran = random.choice(choose)
        print(ran)

        you = input("\n\nrock(r)   paper(p)   scissor(s) : ")
        you = you.lower()

        if you == ran:
            print("Tie")
            print("You both chose same thing\n")
            print("nobody gets pints\n")

        elif you == "r" and ran == "s":
            print(f"\n you chose ROCK and computer chose SCISSOR")
            your_points = your_points + 1
            print("rock broke the scissor\n")
            print("you won this round")
            print("you got 1 point\n")


        elif you == "s" and ran == "r":
            print(f"\n you chose SCISSOR and computer chose ROCK")
            computer_points = computer_points + 1
            print("rock broke the scissor\n")
            print("computer won this round")
            print("computer got 1 point\n")


        elif you == "p" and ran == "r":
            print(f"\n you chose PAPER and computer chose ROCK")
            your_points = your_points + 1
            print("paper wrap the rock\n")
            print("you won this round")
            print("you got 1 point\n")


        elif you == "r" and ran == "p":
            print(f"\n you chose ROCK and computer chose PAPER")
            computer_points = computer_points + 1
            print("paper wrap the rock\n")
            print("computer won this round")
            print("computer got 1 point\n")


        elif you == "s" and ran == "p":
            print(f"\n you chose SCISSOR and computer chose PAPER")
            your_points = your_points + 1
            print("scissor cut the paper\n")
            print("you won this round")
            print("you got 1 point\n")

        elif you == "p" and ran == "s":
            print(f"\n you chose PAPER and computer chose SCISSOR")
            computer_points = computer_points + 1
            print("scissor cut the paper\n")
            print("computer won this round")
            print("computer got 1 point\n")

        else:
            print("invlid input")
            continue

        print("\nno. of guesses left {}".format(n - attempt))
        attempt = attempt + 1

    if attempt > n:
        print("\ngame over\n")
        print(f"your score :{your_points} \ncomputer score :{computer_points}")

    if computer_points > your_points:
        music_loop('lose.mp3', 'stop')
        print("\nYOU LOOSE by", computer_points - your_points, "points\n")
    elif your_points > computer_points:
        music_loop('win.mp3', 'stop')
        print("\nYOU WIN by", your_points - computer_points, "points\n")
    else:
        print("\nits a Tie\n")

    print(n+1 - attempt, "no. of guesses left")
    attempt = attempt + 1

def play_again():
    press = input("press y to play again otherwise press n :")
    print(press.lower())
    if press == "y":
        game()
    else:
        print("see you later")

n = int(input("how many times you wanna play :"))
game()
play_again()






