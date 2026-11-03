print("...Number Guessing Game...")
import random
print("...Welcome to the Number Guessing Game!...")
target_number = random.randint(1, 100)
#print("Target_number:", target_number)
attempts = 0
while True:
  guess = int(input("Guess the number (between 1 and 100): "))
  print("Guess:", guess)
  attempts += 1
  if guess < target_number:
    print("Too low! Try again.")
  elif guess > target_number:
    print("Too high! Try again.")
  else:
    print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
    break 
