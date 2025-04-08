import random

guess_chances = 5
chances = 0
random_number = random.randint(1, 10)
print(random_number)

while chances < guess_chances:
   guess_number = int(input("Enter Your Number: "))
   chances += 1
   if guess_number == random_number:
     print(f"🎉 Congratulations! You guessed the correct number in {chances} chances!")
     break
   elif(chances >= guess_chances and random_number!= guess_number):
     print("No more chances! Try again")
   elif guess_number > random_number:
      print("📈 Your guess is too high!")
   else:
      print("Your guess is too low")        