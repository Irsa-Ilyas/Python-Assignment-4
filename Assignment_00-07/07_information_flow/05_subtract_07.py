def subtract_seven(number):
    res=number - 7
    return res


def main():
    number = int(input("Enter a number: "))  
    result = subtract_seven(number)  
    print("Result after subtracting 7:", result)
if __name__ == '__main__':
    main()