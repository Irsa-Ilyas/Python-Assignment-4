def is_adult(age):
    if age >18:
        return True
    return False
def main():
    age : str = int(input("How old is this person?: "))

    result=is_adult(age)
    print(result)
if __name__ == "__main__":
    main()
