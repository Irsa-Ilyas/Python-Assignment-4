def print_divisors(user_input):
    for i in range(1,user_input+1):
        if user_input%i==0:
           print(i ,end=" ")
    


def main():
    user_input=int(input("Enter a num: "))
    res=print_divisors(user_input)
    

if __name__ == '__main__':
    main()
   