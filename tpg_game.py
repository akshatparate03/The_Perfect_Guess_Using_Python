import random
n  = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number between 1 and 100: "))
    if(a > n):
        print("Lower number Please")
        guesses += 1
    elif(a < n):
        print("Higher number Please")
        guesses += 1
print(f"Congratulations, You have guessed the correct number {n} in {guesses} attempts!")
