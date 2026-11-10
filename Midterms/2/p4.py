# Made By Ricky L.
def get_ranked_apartments(filename):
    """Return listing IDs ordered from highest to lowest desirability score."""
    #Do not use sorted() or list.sort().
    # Write your solution here.
    apartment_desires = {}
    apartment_ids = []

    file = open(filename,"r")
    

    address,nghbr,id,rent,time,size = "","",0,0,0,0
    linecount = 0

    for line in file:
        linecount += 1
        if linecount == 1:
            address = line.strip()
        elif linecount == 2:
            nghbr = line.strip()
        elif linecount == 3:
            id = int(line.strip())
        elif linecount == 4:
            rent = float(line.strip())
        elif linecount == 5:
            time = float(line.strip())
        elif linecount == 6:
            size = float(line.strip())
            desire = (size*0.20) - (rent*0.03) - (time*1.00)
            apartment_desires[id] = desire
            apartment_ids.append(id)
            linecount = 0

    while True:
        sorted = True
        for i in range(len(apartment_ids)-1):
            id1,id2 = apartment_ids[i],apartment_ids[i+1]
            if apartment_desires[id1] < apartment_desires[id2]:
                apartment_ids[i],apartment_ids[i+1] = apartment_ids[i+1],apartment_ids[i]
                sorted = False

        if sorted: break

    return apartment_ids


    
