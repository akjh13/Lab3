import lab2.bmi as bmi
import pytest
from lab2.bmi import calculate_bmi  # replace 'your_module_name' with the actual module name

# Test for BMI in the "Normal Weight" range
def test_bmi_normal_weight():
    result = calculate_bmi(height=1.73, weight=57)  # BMI is approximately 19.04
    assert result == 0, "Expected Normal Weight classification (0)"

# Test for BMI in the "Over Weight" range
def test_bmi_over_weight():
    result = calculate_bmi(height=1.6, weight=75)  # BMI is approximately 29.3
    assert result == 1, "Expected Over Weight classification (1)"

# Test for BMI in the "Under Weight" range
def test_bmi_under_weight():
    result = calculate_bmi(height=1.8, weight=50)  # BMI is approximately 15.4
    assert result == -1, "Expected Under Weight classification (-1)"

