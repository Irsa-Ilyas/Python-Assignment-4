def main():
    user_input=input("Enter your name: ")
    print(greet(user_input))
    

def greet(user_input):
    return  " Hello " + user_input
if __name__ == '__main__':
    main()