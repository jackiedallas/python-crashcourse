import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('jackie', 'dallas', 100000)
    return employee

def test_give_default_raise(employee):
    """Test that the default raise function works."""
    employee.give_raise()
    assert employee.salary == 105000

def test_give_custom_raise(employee):
    """Test that giving a custom raise works."""
    employee.give_raise(500)
    assert employee.salary == 100500
