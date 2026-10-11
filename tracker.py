# Charity shop stock tracker
def load_items():
    items = []
    with open ("items.csv", "r") as file:
        file.readline()
        line = file.readline().rstrip('\n')
        while line:
            row = line.split(",")
            items.append(row)
            line = file.readline().rstrip('\n')
        return items

print (load_items())
        