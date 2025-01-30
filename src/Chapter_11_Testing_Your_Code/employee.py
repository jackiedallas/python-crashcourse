"""
employee.py
@author: Jackie Johnson-Dallas
This class should take in a first name, a last name, and an annual salary, and
store each of these as attributes.
"""


class Employee:
    """Collect employee information."""
    def __init__(self, first_name, last_name, salary):
        """Store first name, last name, and salary."""
        self.first = first_name
        self.last = last_name
        self.salary = int(salary)
    
    def give_raise(self, salary=''):
        """
        Give a raise to the employee, if no salary argument default to
        5000.
        """
        if salary:
            self.salary += salary
        else:
            self.salary += 5000