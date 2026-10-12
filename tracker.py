# Charity shop stock tracker
def load_items():
    inv = []
    with open ("items.csv", "r") as file:
        file.readline()
        line = file.readline().rstrip('\n')
        while line:
            row = line.split(",")
            inv.append(row)
            line = file.readline().rstrip('\n')
        return inv

def save_items(inv):
    file = open("items.csv", "w")
    file.write("item,category,date_donated,price,sold\n")
    for row in inv:
        line = ",".join(row)
        file.write(line + "\n")
    file.close()

def add_items(inv):
    name = input("Item name: ")
    category = input("Category: ")
    date = input("Date donated (YYYY-MM-DD): ")
    price = input("Price is £: ")
    row = [name, category, date, price, "no"]
    inv.append(row)
    save_items(inv)
    print("Item added")

inv = load_items()
add_items(inv)