def main():
    num_counts={}
    while True:
        user_input=int(input("\033[94mEnter a number (or press Enter to stop): \033[0m"))
        if user_input == "":
           break
        if user_input in num_counts:
            num_counts[user_input]+=1
        else:
            num_counts[user_input]+1
        for num,count in num_counts.items():
            print(f"{num} appers {count} times.")
if __name__ == '__main__':
    main()           




