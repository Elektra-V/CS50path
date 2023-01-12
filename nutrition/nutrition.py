def main():
    fruit_name = input("Item: ").lower()
    calories = check_calories(fruit_name)
    if calories is None:
        return 1

    print(f"Calories: {calories}")


def check_calories(fruit: str) -> int:
    fruit_dict = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwi fruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    if fruit in fruit_dict.keys():
        return fruit_dict[fruit]


if __name__ == "__main__":
    main()

