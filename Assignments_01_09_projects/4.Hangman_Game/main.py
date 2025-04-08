import random

searchlist = ["hyper", "Text", "Mark", "Up", "Language"]
computerchose = random.choice(searchlist).lower()
print(computerchose)
computerset = set(computerchose)
print(computerset)
myset = set()
attempts = 6

while attempts > 0 and computerset:
    display = [word if word in myset else "_" for word in computerchose]
    print(" ".join(display))

    myinput = input("Guess a letter (A-Z): ").lower()

    if myinput in computerset:
        myset.add(myinput)
        computerset.remove(myinput)
        print("✅  Correct")
    elif myinput in myset:
        print("❗ Already guessed")
    elif myinput not in computerset:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} attempts left")

if not computerset:
    print("🎉 Congratulations! You Win")
else:
    print(f"Better luck next time 😔. The correct word is {computerchose.upper()}")
