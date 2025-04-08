def main():
    num1=int(input("Please enter an integer to be divided: "))
    num2=int(input("Please enter an integer to divide by: "))
    quotient=num1//num2
    remainder=num1%num2
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


if __name__ == '__main__':
    main()