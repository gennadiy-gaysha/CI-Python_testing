import unittest
from evens import even_number_of_evens
# our class needs to inherit  from the unittest.TestCase class


class TestEvens(unittest.TestCase):
    # Calling the assertRaises method  from TestCase and when the test is run
    # it checks to see if a TypeError is raised  when the function is called with the value
    # 4. This should fail, as our function  at the moment is set to return None.
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 28]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


# The unittest.main() function is a convenience function provided by the unittest module in Python's standard library.
# When unittest.main() is called, it automatically discovers the test cases defined within the script and runs them.
# It collects all the test cases by searching for classes that inherit from unittest.TestCase and have method names starting with "test_". In this case, the TestEvens class satisfies these conditions and contains the test_function_returns_true method.
if __name__ == "__main__":
    unittest.main()
