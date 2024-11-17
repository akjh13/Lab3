import price_info  # Ensure the correct module name

def test_total_cost_shopping(capsys):
    price_info.total_cost_shopping()
    captured = capsys.readouterr()
    # Ensure the output matches the correct total cost
    assert captured.out.strip() == "Total cost = $ 46.75"

def test_cost_of_fruits_apple(capsys):
    price_info.cost_of_fruits('apple', 10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cost of 10 apple(s) = $ 12.0"

def test_cost_of_fruits_orange(capsys):
    price_info.cost_of_fruits('orange', 7)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cost of 7 orange(s) = $ 9.8"

def test_cost_of_fruits_invalid_fruit(capsys):
    price_info.cost_of_fruits('mango', 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cost of 5 mango(s) = $ 0.0"  # Ensure 0.0 for invalid fruit
