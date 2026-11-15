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
    price = input("Price in £: ")
    while not price.replace(".", "", 1).isdigit():
       print("Please enter a number, like 4.50")
       price = input("Price in £: ")
    row = [name, category, date, price, "no"]
    inv.append(row)
    save_items(inv)
    print("Item added")

def list_items(inv):
    for i in range(len(inv)):
        print(i+1, inv[i][0], inv[i][1], inv[i][2], "£" + inv[i][3], inv[i][4])

def mark_sold(inv):
    list_items(inv)
    text = input("Item number to be marked as sold: ")
    if text.isdigit():
        choice = int(text)
        if choice >= 1 and choice <= len(inv):
            inv[choice - 1][4] = "yes"
            save_items(inv)
            print("Item marked as sold")
        else:
            print("Invalid item number")
    else:
        print("Please enter a number")
        
def generate_report(inv):
    stock_total = 0
    sold_total = 0
    for row in inv:
        if row[4] == "no":
            stock_total = stock_total + float(row[3])
        else:
            sold_total = sold_total + float(row[3])
    total = stock_total + sold_total
    if total > 0:
        sold_percent = sold_total / total * 100
    else:
        sold_percent = 0
    categories = []
    category_totals = []
    for row in inv:
        if row[4] == "yes":
            found = False
            for i in range(len(categories)):
                if categories[i] == row[1]:
                    category_totals[i] = category_totals[i] + float(row[3])
                    found = True
            if not found:
                categories.append(row[1])
                category_totals.append(float(row[3]))
    biggest = 0
    for amount in category_totals:
        if amount > biggest:
            biggest = amount
    file = open("index.html", "w")
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write('<head><title>Shop Stock</title><link rel="stylesheet" href="style.css"></head>\n')
    file.write("<body>\n")
    file.write("<h1>Charity Shop Stock</h1>\n")
    file.write('<div class="dashboard">\n')

    file.write('<div class="left">\n')
    file.write("<h2>Current Inventory</h2>\n")
    file.write("<table>\n")
    file.write("<tr><th>Item</th><th>Category</th><th>Date donated</th><th>Price</th></tr>\n")
    for row in inv:
        if row[4] == "no":
            file.write("<tr><td>" + row[0] + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td><td>&pound;" + row[3] + "</td></tr>\n")
    file.write("</table>\n")
    file.write("<h2>Sold Inventory</h2>\n")
    file.write("<table>\n")
    file.write("<tr><th>Item</th><th>Category</th><th>Date donated</th><th>Price</th></tr>\n")
    for row in inv:
        if row[4] == "yes":
            file.write("<tr><td>" + row[0] + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td><td>&pound;" + row[3] + "</td></tr>\n")
    file.write("</table>\n")
    file.write("</div>\n")

    file.write('<div class="right">\n')
    file.write('<div class="chart-box"><h2>Sales vs Stock</h2><div class="pie" style="background: conic-gradient(#27ae60 0% ' + str(sold_percent) + '%, #2c3e50 ' + str(sold_percent) + '% 100%);"></div><p>Total value: &pound;' + str(round(total, 2)) + '</p><p>Sold: &pound;' + str(round(sold_total, 2)) + ' | In stock: &pound;' + str(round(stock_total, 2)) + '</p></div>\n')
    file.write('<div class="chart-box"><h2>Sales by Category</h2>\n')
    file.write('<div class="v-chart">\n')
    file.write('<div class="v-axis"><span>&pound;' + str(round(biggest, 2)) + '</span><span>&pound;0</span></div>\n')
    for i in range(len(categories)):
        height = category_totals[i] / biggest * 100
        file.write('<div class="v-col"><div class="v-area"><div class="v-bar" style="height: ' + str(height) + '%;"></div></div><span class="v-label">' + categories[i] + '</span><span class="v-value">&pound;' + str(round(category_totals[i], 2)) + '</span></div>\n')
    file.write('</div>\n')
    file.write('</div>\n')

    file.write("</div>\n")
    file.write("</body>\n")
    file.write("</html>\n")
    file.close()
        
inv = load_items()
running = True

while running:
    print("1. Add item")
    print("2. List items")
    print("3. Mark item as sold")
    print("4. Refresh report")
    print("5. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_items(inv)
        generate_report(inv)
    elif choice == "2":
        list_items(inv)
    elif choice == "3":
        mark_sold(inv)
        generate_report(inv)
    elif choice == "4":
        generate_report(inv)
    elif choice == "5":
        running = False
        print("Goodbye")
    else:
        print("Please choose 1, 2, 3, 4 or 5")