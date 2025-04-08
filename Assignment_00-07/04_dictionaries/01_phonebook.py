def read_numbers():
    phonebook = {}
    while True:
        name = input("Enter Name: ")
        if name == "":
            break
        number = input("Enter Number: ")
        phonebook[name] = number  
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in phonebook")
        else:
            print(f"{name}->{phonebook[name]}")

def main():
    phonebook = read_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
