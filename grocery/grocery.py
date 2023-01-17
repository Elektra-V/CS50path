def main():
    
    shop_list = {}
    while True:
        try:
            item = input().upper()
            count = 0
            if item not in shop_list.keys():
                shop_list[item] = 1
            else:
                shop_list[item] += 1
        
        except KeyError:
            pass

        except EOFError:
            print("\n")
            new_list = dict(sorted(shop_list.items()))
            for key in new_list:
                print(new_list[key], key)
            break


main()