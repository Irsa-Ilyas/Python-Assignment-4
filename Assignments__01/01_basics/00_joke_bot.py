def abc(user_input):
    joke = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
    sorry= "Sorry I only tell jokes"
    if user_input.lower() == "joke":
        print(joke)  
    else:
        print(sorry)

def main():
    user_input = input("What do you want?")

    res=abc(user_input)
    return res
if __name__ == '__main__':
    main()