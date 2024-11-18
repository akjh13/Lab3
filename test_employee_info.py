import employee_info

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected_result = 361000 / 6  # Correct total salary divided by count
    assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(22, 31)
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_get_employees_by_dept():
    department = "Marketing"
    result = employee_info.get_employees_by_dept(department)
    expected_result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    assert result == expected_result, f"Expected {expected_result}, got {result}"
