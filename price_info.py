price_list = {
    'apple': 1.20,
    'orange': 1.40,
    'watermelon': 6.50,
    'pineapple': 2.70,
    'pear': 0.90,
    'papaya': 2.95,
    'pomegranate': 4.95
}

quantity_list = {
    'apple': 5,
    'orange': 5,
    'watermelon': 1,
    'pineapple': 2,
    'pear': 10,
    'papaya': 1,
    'pomegranate': 2
}

def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            total_cost += price_list[key] * quantity_list[key]#changes made is this line
    
    # Round the total cost to 2 decimal places, and print correctly
    print(f"Total cost = $ {round(total_cost, 2)}")


def cost_of_fruits(fruit, quantity):
    if fruit in price_list:
        cost = quantity * price_list[fruit]
    else:
        cost = 0.0  # Ensure we return 0.0 for non-existent fruits
    
    # Round and format output correctly to 2 decimal places
    print(f"Cost of {quantity} {fruit}(s) = $ {round(cost, 2)}")

def main():
    cost_of_fruits('apple', 10)
    total_cost_shopping()

if __name__ == "__main__":
    main()
