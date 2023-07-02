from application.salary import *
from application.db.people import *
import datetime
import requests





if __name__ == '__main__':
    print(datetime.date.today())
    
    print (get_employees())

    print (calculate_salary())

    