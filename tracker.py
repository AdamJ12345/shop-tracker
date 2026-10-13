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
        
def generate_report(inv):
    file = open("index.html", "w")
    file.write("<html>\n")
    file.write('<head><title>Shop Stock</title><link rel="stylesheet" href="style.css"></head>\n')
    file.write("<body>\n")
    file.write("<h1>Charity Shop Stock</h1>\n")
    file.write("<h2>Current Inventory</h2>\n")
    file.write("<table>\n")
    file.write("<tr><th>Item</th><th>Category</th><th>Date donated</th><th>Price</th></tr>\n")
    for row in inv:
        if row[4] == "no":
            file.write("<tr><td>" + row[0] + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td><td>&pound;" + row[3] + "</td></tr>\n")
    file.write("</table>\n")
    file.write("<h2>Sold Items</h2>\n")
    file.write("<table>\n")
    file.write("<tr><th>Item</th><th>Category</th><th>Date donated</th><th>Price</th></tr>\n")
    for row in inv:
        if row[4] == "yes":
            file.write("<tr><td>" + row[0] + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td><td>&pound;" + row[3] + "</td></tr>\n")
    file.write("</table>\n")
    file.write("</body>\n")
    file.write("</html>\n")
    file.close()
            
        
inv = load_items()
running = True

while running:
    print("1. Add item")
    print("2. List items")
    print("3. Mark item as sold")
    print("4. Generate report")
    print("5. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_items(inv)
    elif choice == "2":
        list_items(inv)
    elif choice == "3":
        mark_sold(inv)
    elif choice == "4":
        generate_report(inv)
    elif choice == "5":
        running = False
        print("Goodbye")
    else:
        print("Please choose 1, 2, 3 or 4")