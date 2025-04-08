import random
n_numbers = 10
min_value = 1
max_value = 100
def main():
    for i in range(n_numbers):
        random_num = random.randint(min_value, max_value)
        print(f"{random_num}" , end=" " )
if __name__ == '__main__':
    main()
