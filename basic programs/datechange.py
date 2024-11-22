from datetime import datetime, timedelta

def addDate(days):
    today = datetime.now()
    changed_date = today + timedelta(days=days)
    return changed_date.strftime("%d-%m-%Y")

def main():
    days = int(input("Enter the number of days: "))
    changed_date = addDate(days)
    print(changed_date)

if __name__ == "__main__":
    main()