# from db import *
from application.salary import calculate_salary
from application.db.people import get_emloyees


if __name__ == '__main__':
    calculate_salary()
    get_emloyees()