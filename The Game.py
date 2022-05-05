from threading import Timer
from random import *
from time import *
from os import system
from sys import stdout

timeout = 15
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
key = 3
newMessage = ""
jumble = False
questions = ["What gets wet as it drys?: ", "Who owns the territory of Puerto Rico?: ", "What is 9x12?: ", "What has hands, but no legs, cannot move, but always chimes?: ", "What actor plays Maui in Moana?: ", "Who was the 43rd President of the United States?: ", "A bird in the hand is worth?: ", "Who is the host of Family Feud?: ", "Who is the only rapper to win a pulitzer prize?: ", "what is 12 squared?: "]
answers = ["Towel", "United States", "108", "Clock", "Rock", "George W. Bush", " Two in the bush", "Steve Harvey", "Kendrick Lamar", "144"]


def animate(text, newLine = True, speed=0.025):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        sleep(speed)
    if newLine == True:
        stdout.write("\n")
        stdout.flush()


def givePunishment():
    chance = randint(0, 100)
    animate("Your punishment is...")
    if chance < 50:
        jumble = True
        animate("Jumble, the letters are moved, three back is the key.")
    else:
        animate("The odds were in your favor, you got lucky this time, no punishment.")
    animate("Alright, back to it")
    sleep(1)


animate("Welcome to the game")
animate("What is your name?: ")
Name = input()
animate(Name + ", welcome to your doom!")

def gameStart():
    while True:
    
        t = Timer(timeout, failure)
        t.start()
        position = randint(0, len(questions) - 1)
        prompt = questions[position]
        animate(prompt)
        answer = input()
        t.cancel()
        if jumble == False:
            animate("Your answer was " + answer)
        else:
            animate("Your answer was " + answer)
        sleep(2)
        if answer != answers[position]:
            print("Wrong answer!")
            givePunishment()
        else:
            animate("Correct!")
        sleep(1)


        animate("Take a breather.")
        sleep(2)
        animate("Doing okay?")
        sleep(2)
        animate("Feeling dread yet?")
        sleep(3)
        animate("Time's up! Back to it")
        sleep(1)
    
def failure():
    animate("Time's up! You failed")
    sleep(1)
    animate("Are you prepared for your punishmnent?")
    sleep(1)
    givePunishment()
    gameStart()

gameStart()
