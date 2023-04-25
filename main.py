# This is a sample Python script.
from student_repo import read_students


def say_hello():
    print("HELLO EYEBALLS")


if __name__ == '__main__':
    students = read_students()
    print("***********************  main  **************************")
    for student in students:
        print(student)


