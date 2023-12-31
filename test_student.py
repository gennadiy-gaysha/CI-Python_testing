import unittest
from student import Student
# Import the 'date' class and 'timedelta' from 'datetime'
from datetime import timedelta


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(10)

        self.assertEqual(self.student.end_date,
                         old_end_date + timedelta(days=10))


if __name__ == "__main__":
    unittest.main()
