#Joe Melia EET-107
def main():
    day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    sales = []
    print("Daily Sales Tracker\n")
    for d in day:
        sale = int(input(f"Enter the sales amount for {d}: "))
        sales.append(sale)
    receipt(sales, day)

def receipt(sales, day):
    total = sum(sales)
    hDay = day[sales.index(max(sales))]
    lDay = day[sales.index(min(sales))]
    print(f"\nTotal Weekly Sales: ${float(total):.2f}")
    print(f"Average Weekly Sales: ${(total / len(sales)):.2f}")
    print(f"\nThe highest sales were ${float(max(sales)):.2f} on {hDay}")
    print(f"The lowest sales were ${float(min(sales)):.2f} on {lDay}")
main()
