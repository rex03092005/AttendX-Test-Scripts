
import unittest

def mark_attendance(student_id):
    return student_id != ""

class AttendanceTest(unittest.TestCase):
    def test_valid_student(self):
        self.assertTrue(mark_attendance("STU101"))

    def test_empty_student_id(self):
        self.assertFalse(mark_attendance(""))

if __name__ == "__main__":
    unittest.main()
