#print a list of all divisors of a number

def getDivisors(num):
    list = []
    for i in range(num):
        if i >= 1:
            if ((num % i) == 0):
                list.append(i)
    return list

def main():
    print("Enter a number, and get all factors of the number")
    flag = True

    while flag:
        number = input("What number would you like to factor? \n")
        if number.isdigit():
            number = int(number)
            flag = False

    divisors = 0
    divisors = getDivisors(number)

    print("The factors of your number are: \n")
    print(divisors)
main()
