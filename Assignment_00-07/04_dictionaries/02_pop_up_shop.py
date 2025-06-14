def main():
    # Dictionary storing fruit prices (per unit)
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }
    total_cost=0
    for myfruits, price in fruit_prices.items():
        quantity=int(input(f"How many ({myfruits}) do you want?: "))
        total_cost += quantity*price
    print(f"\nYour total is ${total_cost:.2f}")
    print("Come Again Next Time")
if __name__ == '__main__':
    main()
