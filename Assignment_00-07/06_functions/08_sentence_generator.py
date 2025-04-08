def sentence_generator(user_input,user_ans):
    if user_ans==0:
           print(f"I am excited to add this {user_input} to my vast collection of them!")
       
    elif user_ans==1:
         print(f"It's so nice outside today it makes me want to {user_input}!")
    elif user_ans==2:
        print(f"Looking out my window, the sky is big and {user_input}")
    else:
        print("Please choose 0 1 and 2")        
def main():
    user_input=input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective? ")
    user_ans=int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    sentence_generator(user_input,user_ans)
if __name__ == "__main__":
    main()
