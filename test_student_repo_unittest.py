import datetime
from unittest import TestCase

from sqlalchemy import create_engine

import student_repo


class Test(TestCase):

    def setUp(self) -> None:
        super().setUp()
        engine = create_engine("sqlite://", isolation_level="AUTOCOMMIT")
        con = engine.raw_connection()

        with open('sql/create_tables.sql') as f:
            sql = f.read()
            # hack to make sqlite accept the MySql DDL
            sqlite_compliant_sql = sql.replace('AUTO_INCREMENT', 'AUTOINCREMENT')
            con.executescript(sqlite_compliant_sql)

        student_repo.init(engine)

    def test_add_student(self):
        # AAA - Arrange
        before_students = list(student_repo.read_students())
        student = {
            'lastName': 'Smith',
            'firstName': 'Jane',
            'dob': datetime.date(2000, 1, 1),
            'grade': 12,
            'gpa': None,
            'studentId': 'abcde'
        }
        print(student)

        # AAA - Act
        student_repo.add_student(student)

        # AAA - Assert
        after_students = list(student_repo.read_students())
        self.assertEqual(len(after_students) - len(before_students), 1)

    def test_read_students(self):
        students = student_repo.read_students()
        self.assertEqual([], list(students))
