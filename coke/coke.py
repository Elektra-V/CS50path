def main():
    coke_price = 50
    accepted_coins = [25, 10, 5]

    while True:
        if coke_price <= 0:
            break

        print(f"Amount Due: {coke_price}")
        coin = int(input("Insert Coin: "))

        # Check if inserted coin is accepted by the machine
        if coin in accepted_coins:
            coke_price -= coin

    print(f"Change Owed: {abs(coke_price)}")


if __name__ == "__main__":
    main()

