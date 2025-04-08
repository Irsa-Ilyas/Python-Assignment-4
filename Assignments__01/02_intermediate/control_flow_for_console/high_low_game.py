import random

def main():
    print("Welcome to the High-Low Game!")
    total_rounds = 5
    score = 0

    for round_num in range(1, total_rounds + 1):
        print(f"\nRound {round_num}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print(f"Your number is {user_number}")

        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
            if guess == "higher" or guess == "lower":
                break
            else:
                print("Invalid input! Please enter either 'higher' or 'lower'.")

        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print("You were right!", end=" ")
            score += 1
        else:
            print("Aww, that's incorrect.", end=" ")

        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}")
    print("\n🎮 Game Over!")
    print(f"Total Score: {score}/{total_rounds}")

    if score == total_rounds:
        print("🌟 Wow! You played perfectly!")
    elif score >= total_rounds // 2:
        print("👍 Good job, you played really well!")
    else:
        print("🙁 Better luck next time!")

if __name__ == '__main__':
    main()
