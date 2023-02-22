from datetime import datetime, timedelta
import sys
import inflect

p = inflect.engine()

def main():
    
    dob = input("Date of Birth:  ").strip()
    print(sing_minutes(dob))


def sing_minutes(birthdate: str) -> str:

    if not (date := datetime.strptime(birthdate, "%Y-%m-%d")):
        sys.exit("Invalid date")
     
    else:

        today = datetime.combine(date.today(), datetime.min.time())
        birthday = datetime.combine(date, datetime.min.time())
        diff = today - birthday
        minutes = int(diff/ timedelta(minutes=1))
        sing = p.number_to_words(minutes, andword="").capitalize()
        return f"{sing} minutes."


if __name__ == "__main__":
    main()