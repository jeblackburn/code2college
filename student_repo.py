from sqlalchemy import text, Engine

engine: Engine


def read_students():
    with engine.connect() as connection:
        students = connection.execute(text("select * from student"))
    return students


def add_student(new_student: dict):
    # noinspection SqlResolve
    insert = f"insert into student (studentid, lastname, firstname, dob, grade, gpa) " \
             f"values(:studentid, :lastname, :firstname, :dob, :grade, :gpa)"

    values = {
        'studentid': new_student['studentId'],
        'lastname': new_student['lastName'],
        'firstname': new_student['firstName'],
        'dob': new_student['dob'],
        'grade': new_student['grade'],
        'gpa': new_student['gpa']
    }

    with engine.connect() as conn:
        conn.execute(text(insert), values)


def init(the_engine: Engine):
    global engine
    engine = the_engine
