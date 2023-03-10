from datetime import date
from faker import Faker
from random import randint, sample
import sqlite3

DB = "university.db"

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_EVALUATIONS = 20


def generate_fake_data(number_students: int, 
                       number_groups: int, 
                       number_teachers: int, 
                       number_subjects: int) -> tuple[list]:
    
    faker = Faker()
    
    fake_students = [faker.name() for _ in range(number_students)]
    fake_groups = [faker.company() for _ in range(number_groups)]
    fake_teachers = [faker.name() for _ in range(number_teachers)]
    
    list_subjects = ["English",
                     "math",
                     "art",
                     "science",
                     "history",
                     "music",
                     "geography",
                     "Physical Education",
                     "drama",
                     "biology",
                     "chemistry",
                     "physics",
                     "Information Technology",
                     "foreign languages",
                     "social studies",
                     "technology",
                     "philosophy",
                     "graphic design",
                     "literature",
                     "algebra",
                     "geometry"]
    
    fake_subjects = sample(list_subjects, k=number_subjects)
    # print(f"{fake_subjects=}")
    # quit()
    
    return fake_students, fake_groups, fake_teachers, fake_subjects


def prepare_data(students: list, 
                 groups: list, 
                 teachers: list, 
                 subjects: list) -> tuple[list[tuple]]:
    
    for_students = [(student, randint(1, NUMBER_GROUPS)) for student in students]    
    for_groups = [(group,) for group in groups]
    for_teachers = [(teacher,) for teacher in teachers]
    for_subjects = [(subject, randint(1, NUMBER_TEACHERS)) for subject in subjects]
        
    for_evaluations = []
    
        
    for ns in range(1, NUMBER_STUDENTS+1):
        for _ in range(NUMBER_EVALUATIONS):
            evaluation_date = date(year=2023, month=randint(1, 12), day=randint(1, 20))
            for_evaluations.append((
                randint(60, 100), evaluation_date, 
                ns, randint(1, NUMBER_SUBJECTS)
            ))
            
    return for_students, for_groups, for_teachers, for_subjects, for_evaluations


def insert_data_to_db(students: list[tuple], 
                      groups: list[tuple], 
                      teachers: list[tuple], 
                      subjects: list[tuple], 
                      evaluations: list[tuple]) -> None:
    
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        
        sql_to_students = """
            INSERT INTO Students(Name, Group_id)
            VALUES (?, ?)
        """        
        cursor.executemany(sql_to_students, students)
        
        sql_to_groups = """
            INSERT INTO Groups(Name)
            VALUES (?)
        """
        cursor.executemany(sql_to_groups, groups)
        
        sql_to_teachers = """
            INSERT INTO Teachers(Name)
            VALUES (?)
        """
        cursor.executemany(sql_to_teachers, teachers)
        
        sql_to_subjects = """
            INSERT INTO Subjects(Name, Teacher_id)
            VALUES (?, ?)
        """
        cursor.executemany(sql_to_subjects, subjects)
        
        sql_to_evaluations = """
            INSERT INTO Evaluations(Rating, Date, Student_id, Subject_id)
            VALUES (?, ?, ?, ?)
        """
        cursor.executemany(sql_to_evaluations, evaluations)


if __name__ == "__main__":
    
    fake_data = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    prepare_fake_data = prepare_data(*fake_data)
    insert_data_to_db(*prepare_fake_data)
    