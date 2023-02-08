from datetime import datetime
import faker
from random import randint, choice
import sqlite3


NUMBER_COMPANIES = 3
NUMBER_EMPLOYEES = 30
NUMBER_POST = 5
DATA_BASE = "salary.db"


def generate_fake_data(number_companies, number_employees, number_post):
    
    fake_companies = []
    fake_employees = []
    fake_post = []
    
    fake_data = faker.Faker()
    
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())
        
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())
    
    for _ in range(number_post):
        fake_post.append(fake_data.job())
    
    return fake_companies, fake_employees, fake_post


def prepare_data(companies, employees, posts) -> tuple():
    for_companies = []
    
    for company in companies:
        for_companies.append((company,))
        
    for_employees = []
    
    for employee in employees:
        for_employees.append((employee, choice(posts), randint(1, NUMBER_COMPANIES)))
        
    for_payments = []
    
    for month in range(1, 12+1):
        payments_date = datetime(2023, month, randint(10, 20)).date()
        
        for employee_id in range(1, NUMBER_EMPLOYEES+1):
            for_payments.append((employee_id, payments_date, randint(1000, 10000)))
            
    return for_companies, for_employees, for_payments


def insert_data_to_db(companies, employees, payments) -> None:
    
    with sqlite3.connect(DATA_BASE) as connect:
        
        cursor = connect.cursor()
        sql_to_companies = """
            INSERT INTO companies(company_name)
            VALUES (?)
        """
        cursor.executemany(sql_to_companies, companies)
        
        sql_to_employees = """
            INSERT INTO employees(employee, post, company_id)
            VALUES (?, ?, ?)
        """
        cursor.executemany(sql_to_employees, employees)
        
        sql_to_payments = """
            INSERT INTO payments(employee_id, date_of, total)
            VALUES (?, ?, ?)
        """
        cursor.executemany(sql_to_payments, payments)
        
        connect.commit()
    

if __name__ == "__main__":
    
   fake_data = generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYEES, NUMBER_POST)
   prepare_fake_data = prepare_data(*fake_data)
   insert_data_to_db(*prepare_fake_data)