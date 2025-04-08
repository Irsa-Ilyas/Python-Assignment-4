def main():
    year=int(input("Enetr year to check: "))
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("Leap Year")
            else:
                print("Not a Leap year")
        else:
            print("Leap year")
    else:
        print("not a leap year")        
if __name__ == '__main__':
    main()












