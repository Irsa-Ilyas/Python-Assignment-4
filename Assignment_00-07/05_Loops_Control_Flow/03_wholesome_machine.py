def main():
     affirmation="I can learn Python"
     while True:
      user_input=input("\033[32m Enter anything:\033[0m ")
      if user_input == affirmation:
        print("\033[31m Thats right!\033[0m")
        break
      else:
         print(f"Hmmm That was not the affirmation. Please type the following affirmation:{affirmation}")  
if __name__ == '__main__':
    main()