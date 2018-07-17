#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and
#one number to divide by (check). If check divides evenly into num,
#tell that to the user. If not, print a different appropriate message.
def divisible(num, check):
    return num % check == 0


def main():
    flag = True
    print("Enter two numbers to determine if the first is:")
    print("divisible by the second \n")

    while flag:
        num = 0
        num = input("What is the number you want to check?\n")
        if num.isdigit():
            num = int(num)
            flag = False

    flag = True
    while flag:
        check= 0
        check = input("What would you like to know if it is divisible by?\n")
        if check.isdigit():
            check = int(check)
            flag = False

    div = divisible(num, check)

    if div:
        print(str(num) +" is divisible by " + str(check))
    else:
        print(str(num) + " is not divisible by " + str(check))
        print("The remainder is: " + str(num % check))

main()
