sentence_start = "My superhero name is "
def main():
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    power = input("Enter a superpower: ")

    print(sentence_start + color + " " + animal + " and It can " + power + "!")

if __name__ == '__main__':
    main()
