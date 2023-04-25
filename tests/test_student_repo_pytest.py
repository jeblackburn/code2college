import datetime

import pytest
from sqlalchemy import create_engine, Engine

import student_repo


@pytest.fixture
def engine():
    engine = create_engine("sqlite://", isolation_level="AUTOCOMMIT")
    con = engine.raw_connection()

    with open('../sql/create_tables.sql') as f:
        sql = f.read()
        # hack to make sqlite accept the MySql DDL
        sqlite_compliant_sql = sql.replace('AUTO_INCREMENT', 'AUTOINCREMENT')
        con.executescript(sqlite_compliant_sql)

    return engine


def test_student_repo_add_student(engine):
    student_repo.init(engine)
    student = {
        'lastName': 'Melville',
        'firstName': 'Herman',
        'grade': 10,
        'dob': datetime.datetime(2001, 6, 30),
        'gpa': None,
        'studentId': 'asdf1234'
    }
    student_repo.add_student(student)

    assert student_repo.get_student('asdf1234') == student
