# Activity 4 

# Input the number to be guessed
num = int(input("Please enter the number to be guessed: "))

print("Guess a number between 1 and 100.")
correct = False
times = 0

while not correct:
    times += 1
    guess = int(input("Enter your guess: "))

    # Range Check
    if guess < 0 or guess > 100:
        print("Invalid input! Try again.")
    else:
        # Comparison
        if guess == num:
            print("Hooray! Your answer is correct!")
            correct = True
        elif guess < num:
            print("Your guess is smaller than the actual value.")
        else:
            print("Your guess is greater than the actual value.")

print(f"You guessed {times} times.")