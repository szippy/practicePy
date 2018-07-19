import random
import sys

guesses = 0
flag = True
number = 5
temp = 0
str = ''

def guess():
    flag = True
    while flag:
        num = input("What number am I thinking of?\n")
        num = num.lower()
        if num.isdigit():
            num = int(num)
            return num
            flag = False
        elif num == 'exit':
            sys.exit()

def check(temp, number):
    if temp == number:
        print("Congratulations you won!\n")
        number = random.randint(1,100)
        print("Generating new number....\n")
        print("I'm thinking of a number between 1 and 100. \n")
    elif temp < number:
        print("Your number is too low! Guess Again!\n")
    elif temp > number:
        print("Your number is too high! Guess Again!\n")


number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100. \n")
while flag:

    print("Type 'exit' to give up\n")

    temp = guess()
    check(temp, number)
