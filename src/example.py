# app.py
# This script includes basic arithmetic operations and their test cases

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def mod(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(1, -1) == 2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(10, 0) == "Cannot divide by zero"

def test_mod():
    assert mod(5, 2) == 1
    assert mod(10, 3) == 1
    assert mod(10, 0) == "Cannot divide by zero"

# Running all tests
def run_tests():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_mod()
    print("All tests passed successfully!")

# Run the tests
if __name__ == "__main__":
    run_tests()
