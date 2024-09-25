from unittest import mock
from unittest import TestCase
from testing_example import *

#How do we check code that depends on user input?
#Testing your code using mocks. This example comes from https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
class CreateTests(TestCase):
    @mock.patch('testing_example.input', create=True) #This line indicates that you will overwrite the testing_example.input function.
    def testdictCreateSimple(self, mocked_input):
        print("testdictCreateSimple is running")
        mocked_input.side_effect = ['Albert Einstein', '42.81', 'done'] #This specifies what will be returned by testing_example.input each time it is called.
        result = dictCreate(1) #We call the function that we are testing.
        self.assertEqual(result, {'Albert Einstein': [42.81]}) #We check that the output is what is expected.
        print("test complete")

    @mock.patch('testing_example.input', create=True)
    def testwholeProgram(self, mocked_input):
        print("test is running")
        mocked_input.side_effect = [1,'Albert Einstein', '42.81', 'done']
        result = main()
        self.assertEqual(result, {'Albert Einstein': [42.81]})


#Ok, but how do we check that the correct thing was printed?
#This example comes from ChatGPT
import unittest
import io
import sys

# Example function that prints something
def function_with_print():
    print("Hello, World!")

class PrintStatementTest(unittest.TestCase):
    def test_print_output(self):
        print("test running") 
        # Step 1: Create a StringIO object to capture the output
        captured_output = io.StringIO()
        
        # Step 2: Redirect sys.stdout to the StringIO object
        sys.stdout = captured_output
        
        # Step 3: Call the function that prints something
        function_with_print()
        
        # Step 4: Reset sys.stdout to its original state
        sys.stdout = sys.__stdout__
        
        # Step 5: Check if the printed output is what you expect
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")
        print("test passed")

# if __name__ == "__main__":
#     unittest.main()



# example_test_object = CreateTests()
# example_test_object.testdictCreateSimple()
example_print_statement_test = PrintStatementTest()
example_print_statement_test.test_print_output()