def add_three_copies(messege,mylist):
    mylist.append(messege)
    mylist.append(messege)
    mylist.append(messege)
def main():
    mylist=[]
    messege=input("Enter something: ")
    print("List before",mylist)
    add_three_copies(messege,mylist)
    print("list after",mylist)
if __name__ == '__main__':
    main()
