from application.salary import calculate_salary
from application.db.people import get_emloyees
from application.gt import trans

if __name__ == '__main__':
    calculate_salary()
    get_emloyees()
    trans(input("Введите текст для перевода:"),
          input("Введите язык. по умолчанию -ru:"))
