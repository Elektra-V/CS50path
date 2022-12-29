def main():
  coke_price = 50
  cents = [25, 10, 5]

  while coke_price > 0:
    user_cent = int(input("Insert Coin: "))

    for cent in cents:

      if cent == user_cent:
        coke_price -= cent
        if coke_price > 0:
          print(f"Amount Due: {coke_price}")

  print(f"Change Owed: {abs(coke_price)}")


if __name__ == "__main__":
  main()           