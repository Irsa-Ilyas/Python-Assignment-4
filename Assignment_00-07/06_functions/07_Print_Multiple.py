def print_multiple(user_input,repeat_input):
    for i in range(repeat_input):
        print(user_input)

def main():
    user_input=input("Enter your word to repeat: ")
    repeat_input=int(input("Enter a num to repeat your messege: "))
    res=print_multiple(user_input,repeat_input)

if __name__ == "__main__":
    main()
