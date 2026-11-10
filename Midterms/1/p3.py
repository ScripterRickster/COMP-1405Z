# Made By Ricky L. - NOTE THAT THIS SOLUTION DOES NOT WORK
'''
def sort_string(unsorted_string):
    print(unsorted_string)
    unsorted_string = unsorted_string.strip()
    unsorted = True
    sorted_string = ""
    num1, num2 = "",""
    modded = False
    while unsorted:
        num1_complete,num2_complete = False,False
        for i in range(len(unsorted_string)-1):
            if unsorted_string[i] == " " or i == len(unsorted_string)-1:
                if not num1_complete:
                    num1_complete = True
                    if num1 == "":
                        break
                elif not num2_complete:
                    num2_complete = True

            if i == len(unsorted_string)-1:
                num1_complete = True
                num2_complete = True

            if num1_complete and num2_complete:
                add_begin_space = True
                if sorted_string == "":
                    add_begin_space = False
                    
                if add_begin_space:
                    sorted_string = sorted_string + " "

                if float(num1) < float(num2):
                    sorted_string = sorted_string + num2 + " " + num1
                    print(sorted_string)
                    num2 = ""
                    num1 = ""
                    modded = True
                    
                num1_complete,num2_complete = False,False
                
            if not num1_complete:
                num1 = num1 + unsorted_string[i]
            elif not num2_complete:
                num2 = num2 + unsorted_string[i]
        
        if not modded:
            unsorted = False
        else:
            unsorted_string = sorted_string
            sorted_string = ""

    return sorted_string

## match items to quantity values and thats how u print

def print_sorted_inventory_value(filename):
    file = open(filename,"r")
    linecount = 0
    total_values = ""
    quantity = -1
    price_per_unit = -1
    for line in file:
        if quantity > -1 and price_per_unit > -1:
            if not total_values == "":
                total_values = total_values + " "
                
            total_values = total_values + str(quantity * price_per_unit)
            quantity = -1
            price_per_unit = -1

        linecount += 1
        if linecount % 4 == 0:
            quantity = int(line.strip())
        elif linecount % 5 == 0:
            price_per_unit = float(line.strip())
            linecount = 0

    if quantity > -1 and price_per_unit > -1:
        if not total_values == "":
            total_values = total_values + " "
                    
            total_values = total_values + str(quantity * price_per_unit)
            quantity = -1
            price_per_unit = -1
    

    print(sort_string(total_values))

print_sorted_inventory_value("inventory0.txt")
'''

def get_item_value(file,id):

    for line in file:
        if int(id) == int(line.strip()):
            return int(file.readline().strip) * float(file.readline().strip())
    return 0

def get_item_line(file,id):
    for line in file:
        i1 = file.readline().strip()
        i2 = file.readline().strip()
        i3 = int(file.readline().strip())
        i4 = int(file.readline().strip())
        i5 = float(file.readline().strip())
        if int(id) == i3:
            return i1 + ", " + i2 + ", " + str(i4*i5)
    return ""


def sort_by_ids(id_list):
    unsorted = True

    sorted_id_list = ""

    while unsorted:
        curr_id = ""
        next_id = ""
        cc,nc = False,False
        mods = False

        for i in range(len(id_list)-1):
            if id_list[i] == " ":
                if not cc:
                    cc = True
                elif not nc:
                    nc = True

                if cc and nc:
                    val1,val2 = get_item_value(curr_id),get_item_value(next_id)

                    if val2 > val1:
                        if sorted_id_list != "": sorted_id_list = sorted_id_list + " "
                        sorted_id_list = val2 + " " + val1
                        mods = True
                    curr_id = next_id
                    next_id = ""
                    nc = False
        
        if not mods:
            unsorted = True

    
def print_by_ids(id_list):
    id = ""

    for i in range(len(id_list)-1):
        if id != " " and id_list[i] == " ":
            print(get_item_line(id))
            id = ""
        else:
            id = id + id_list[i]

def print_sorted_inventory_value(filename):
    file = open(filename,"r")

    id_list = ""
    linecount = 0
    for line in file:
        linecount += 1

        if linecount % 3 == 0:
            linecount = 0
            i3 = int(line.strip())
            if id_list != "":
                id_list = id_list + " "
                id_list = id_list + str(i3)

            

    sorted_ids = sort_by_ids(id_list)
    print_by_ids(sorted_ids)
    




print_sorted_inventory_value("inventory0.txt")





