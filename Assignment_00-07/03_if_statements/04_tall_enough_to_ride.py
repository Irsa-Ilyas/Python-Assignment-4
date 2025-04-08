def main():
    while True:
        height=int(input("How tall are you? "))
         
        if height<=20:
           print("You are tooo small")
           break
        if height >=50:
           print("You're tall enough to ride!")
        else:
           print("You're not tall enough to ride, but maybe next year!")
if __name__ == '__main__':
    main()