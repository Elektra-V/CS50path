def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        
        try:

            in_date = input("Date: ").title().strip()
            l = []
            if '/' in in_date:
                date = in_date.split('/')
                l += date

            elif ',' in in_date:
                date = in_date.replace(',',' ').split()
                for i in range(len(months)):
                    if date[0] == months[i]:
                        date[0] = i+1
                        date[1] = int(date[1])
                        date[2] = int(date[2])
                l += date
            month = int(l[0])
            day = int(l[1])
            year = l[2]

            if (1<month<13) and (1<day<32):
                print(f"{year}-{month:02}-{day:02}")
                break
            
        except ValueError:
            pass

        except IndexError:
            pass


main()