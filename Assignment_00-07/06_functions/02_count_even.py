
def count_even(lst):
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    # Here's another way to do this same thing, with a different kind of for-loop:
    # for i in range(len(lst)):
    #     num = lst[i]
    #     if num % 2 == 0:
    #         count += 1

    print(count)  
def get_list_of_ints():
   
    lst = []  
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  
        lst.append(int(user_input))  
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == '__main__':
    main()