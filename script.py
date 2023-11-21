def split_bill(items, tax, tip, allocations):
    """
    items: dict, key = item name, value = price
    tax: float, total tax amount
    tip: float, total tip amount
    allocations: dict, key = person's name, value = list of items they bought
    """
    total_bill = sum(items.values()) + tax + tip
    individual_totals = {person: 0 for person in allocations}
    
    # Calculate individual totals for items
    for person, items_bought in allocations.items():
        for item in items_bought:
            individual_totals[person] += items[item]
    
    # Calculate total without tax and tips for proportion calculation
    total_excluding_tax_tip = sum(items.values())

    # Add proportional tax and tip to each individual's total
    for person in individual_totals:
        proportion = individual_totals[person] / total_excluding_tax_tip
        individual_totals[person] += (tax + tip) * proportion
    
    return individual_totals

# Example usage
items = {"milk": 3.50, "bread": 2.00, "eggs": 1.50}
tax = 0.50
tip = 1.00
allocations = {"Alice": ["milk", "bread"], "Bob": ["eggs"]}

bill_split = split_bill(items, tax, tip, allocations)
print(bill_split)
