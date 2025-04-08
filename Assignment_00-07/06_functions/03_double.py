def double_num(num):
    a=num*2
    return a
def main():
    num=int(input("Enter number: "))
    result=double_num(num) 
    print(f"The doubled number is {result}")
if __name__ == '__main__':
    main()      