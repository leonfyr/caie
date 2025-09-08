while True:
    Mark = int(input("Enter your exam mark"))
    if Mark < 40:
        Grade = "Fail"
    elif Mark < 60:
        Grade = "Pass"
    elif Mark < 80:
        Grade = "Merit"
    else:
        Grade = "Distinction"

    print("Your grade is ", Grade)

    Reply = input("Enter another exam mark Y/N")
    if Reply == "N":
        break

###

Password = ""
while True:
    Password = input("Please set the password:")
    Check = input("Please re-enter the password:")
    if Check != Password:
        print("The password doesn't match! Try again!")
    else:
        break
print("The password is set successfully. ")

Correct = False
for Counter in range(3):
    Check = input("Please enter the password:")
    if Check == Password:
        print("Password correct!")
        Correct = True
        break
    else:
        print("Incorrect. ")