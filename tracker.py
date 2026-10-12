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

def list_items(inv):
    for i in range(len(inv)):
        print(i+1, inv[i][0], inv[i][1], inv[i][2], "£" + inv[i][3], inv[i][4])

def mark_sold(inv):
    list_items(inv)
    choice = int(input("Item number to be marked as sold: "))
    if choice >= 1 and choice <= len(inv):
        inv[choice - 1][4] = "yes"
        save_items(inv)
        print("Item marked as sold")
    else:
        print("Invalid item number")
        
