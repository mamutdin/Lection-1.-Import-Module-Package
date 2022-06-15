from application.salary import calculate_salary
from application.db.people import get_employees

import datetime

def main():
   print("main function")

def current_date():
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()
    current_date()