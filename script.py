def get_input():
    items = {}
    allocations = {}
    while True:
        item = input("Enter item name (or 'done' to finish): ").strip()
        if item.lower() == 'done':
            break

        price = float(input(f"Enter price for {item}: "))
        items[item] = price

        buyers = input(f"Enter names of buyers for {item} separated by commas: ").split(',')
        for buyer in buyers:
            buyer = buyer.strip()
            if buyer in allocations:
                allocations[buyer].append(item)
            else:
                allocations[buyer] = [item]

    tax = float(input("Enter total tax amount: "))
    tip = float(input("Enter total tip amount: "))

    return items, tax, tip, allocations

def split_bill(items, tax, tip, allocations):
    total_bill = sum(items.values()) + tax + tip
    individual_totals = {person: 0 for person in allocations}
    
    for person, items_bought in allocations.items():
        for item in items_bought:
            individual_totals[person] += items[item] / len(allocations)
    
    total_excluding_tax_tip = sum(items.values())

    for person in individual_totals:
        proportion = individual_totals[person] / total_excluding_tax_tip
        individual_totals[person] += (tax + tip) * proportion
    
    return individual_totals

def main():
    items, tax, tip, allocations = get_input()
    bill_split = split_bill(items, tax, tip, allocations)
    for person, total in bill_split.items():
        print(f"{person} owes: ${total:.2f}")

if __name__ == "__main__":
    main()
