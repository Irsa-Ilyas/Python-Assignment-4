import random
print("Welcome to the game")
userlist=["rock","scissors","paper"]
randomchoose=random.choice(userlist).lower()

user=input("choose rock, paper, scissors").lower()
print("You Choose:",user)
print("Computer Choose: ",randomchoose)
if user not in userlist:
  print(" ❌ Invalid choice! Please choose Rock, Paper, or scissors. ❌ ")
elif user == randomchoose:
  print("It's Tie! Try again. 🔄 ")
elif((user == "rock" and randomchoose == "scissors") or (user == "scissors" and randomchoose == "paper") or (user == "paper" and randomchoose == "rock")):
 print("You Win! 🏆")
else:
 print("❌ You Lose Better Luck Next Time")