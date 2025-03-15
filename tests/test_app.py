import pytest

from  myapp.app import multiply_by_two, divide_by_two, calculate_area



@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

def test_calculate_area():
    assert calculate_area(4) == 16 
    assert calculate_area(5) == 25  
    assert calculate_area(0) == 0   

def test_invalid_input():
    import pytest
    with pytest.raises(ValueError):
        calculate_area(-5)  
    with pytest.raises(ValueError):
        calculate_area("abc")

def test_student_id_calculation():
    
    assert multiply_by_two(11.5) == 23  # Student Id = 100932523