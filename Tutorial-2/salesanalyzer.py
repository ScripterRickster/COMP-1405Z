'''

Made By Ricky L.

Purchase #1 Customer Name
Purchase #1 Number of Desktops
Purchase #1 Number of Laptops
Purchase #1 Number of Tablets
Purchase #1 Number of Toasters
Purchase #1 Total Cost
'''

def get_number_purchases(filename):
    if not filename: return 0
    f = open(filename,"r")

    lines = 0

    for l in f:
        lines += 1

    f.close()

    return lines//6

def get_total_purchases(filename):
    if not filename: return 0
    f = open(filename,"r")

    total = 0
    lines = 0

    for l in f:
        lines += 1
        if lines%6 == 0:
            total += int(str(l).strip())


    f.close()

    return total

def get_average_purchases(filename):
    if not filename: return 0
    f = open(filename,"r")

    total = 0
    lines = 0

    for l in f:
        lines += 1
        if lines%6 == 0:
            total += int(str(l).strip())


    f.close()
    if lines == 0: return 0
    if total%lines//6 == 0:
        return total//(lines//6)
    else:
        return round(total/(lines//6),2)

def get_number_customer_purchases(filename,customer):
    if not filename or not customer: return 0

    f = open(filename,"r")

    purchases = 0

    for l in f:
        if l.strip().lower() == customer.lower():
            purchases += 1


    f.close()
    return purchases


def get_total_customer_purchases(filename,customer):
    if not filename or not customer: return 0

    f = open(filename,"r")

    total = 0
    lines = 0
    add = False

    for l in f:
        lines += 1
        if l.strip().lower() == customer.lower():
            add = True
        if add and lines%6 == 0:
            total += int(str(l).strip())
            add = False


    f.close()
    return total

def get_average_customer_purchases(filename,customer):
    if not filename or not customer: return 0

    f = open(filename,"r")

    total = 0
    lines = 0
    purchases = 0
    add = False

    for l in f:
        lines += 1
        if l.strip().lower() == customer.lower():
            add = True
            purchases += 1
        if add and lines%6 == 0:
            total += int(str(l).strip())
            add = False


    f.close()
    if purchases == 0: return 0
    if total%purchases == 0:
        return total//purchases
    else:
        return round(total/purchases,2)


def get_most_popular_product(filename):
    if not filename: return ""

    f = open(filename,"r")

    products = [0,0,0,0] # desktops, laptops, tablets, toasters

    lines = 0
    product = ""
    for l in f:
        lines += 1
        if lines%6 >= 2 and lines%6 <= 5:
            amount = int(str(l).strip())
            products[lines%6-2] += amount

    f.close()

    max_product = ""
    max_count = 0
    for i in range(len(products)):
        if products[i] > max_count:
            max_count = products[i]
            if i == 0:
                max_product = "Desktop"
            elif i == 1:
                max_product = "Laptop"
            elif i == 2:
                max_product = "Tablet"
            elif i == 3:
                max_product = "Toaster"

    return max_product

