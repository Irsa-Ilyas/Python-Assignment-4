import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
import random

low_number = 1
high_number = 20
attempt = 0

print("🎯 Think of a number between 1 and 20! I'll try to guess it! 🤖")

while True:
    if low_number > high_number:
        print("⚠️ Something went wrong! Did you change your number? 😲")
        break
    attempt += 1
    generate_random = random.randint(low_number, high_number)  # Generate a new guess
    print(f"🤖 My guess is: {generate_random}")
    user_guess = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

    if user_guess == "c":
        print(f"🎉 Congratulations! I guessed your number in {attempt} attempts! 🎉")
        break
    elif user_guess == "l":
        low_number = generate_random + 1  # Update lower range
    elif user_guess == "h":
        high_number = generate_random - 1  # Update upper range
    else:
        print("⚠️ Please enter 'H', 'L', or 'C' only!")
