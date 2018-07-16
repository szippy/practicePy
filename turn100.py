#Get user age

print("Running: 'What Year Will You Turn 100'")
year = 0

flag = True
while flag:
    name = input("What is your name? \n")
    if not name.isdigit():
        flag = False

flag = True
while flag:
    year = input("What year were you born? \n")
    if year.isdigit():
        flag = False
        year = int(year)

#you will turn 100 100 years after you were born
year = year + 100

print("You, " + name + ", will turn 100 in ")
print(year)
