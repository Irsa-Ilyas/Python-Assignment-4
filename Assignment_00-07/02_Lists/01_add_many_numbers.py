def sum_of_numbers(abc):
    total=0
    for i in abc:
        total+=i
    return total
def main():
    numbers=[10,10,10,10,10]
    result=sum_of_numbers(numbers)
    print("My List: "+str(numbers))
    print("Result: "+str(result))
if __name__ == '__main__':
    main()













