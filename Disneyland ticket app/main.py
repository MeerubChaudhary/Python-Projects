




def main():
    numGuests = 0
    guestAge = 0
    guestType = ""
    numToddler = 0
    numChild = 0
    numAdult = 0
    totalToddlerCost = 0
    totalChildCost = 0
    totalAdultCost = 0
    totalCostForAll = 0


    numGuests = int(input("How many guests in your party? (Limit 8 guests per party): "))
    while numGuests > 8 or numGuests < 1:
        numGuests = int(input("How many guests in your party? (Limit 8 guests per party): "))
    
    for i in range(numGuests):
        guestAge = int(input(f"Enter age of guest {i + 1}: "))
        guestType = get_guest_type(guestAge)
        if guestType =='t':
            numToddler += 1
        elif guestType == 'c':
              numChild += 1
        else:
            numAdult += 1
    totalToddlerCost = 0
    totalChildCost = numChild * 125
    totalAdultCost = numAdult * 155
    totalCostForAll = totalAdultCost + totalChildCost + totalToddlerCost
        
    print("")
    print("Ticket type\t \t \t    QTY \tCost")
    print("------------------------------------------------------")
    print(f"Adult (ages 10 and up) - $155.00     {numAdult}         {totalAdultCost:.2f}")
    print(f"Child (ages 3- 9) - $125.00          {numChild}         {totalChildCost:.2f}")
    print(f"Toddler (ages 0 -2) - FREE           {numToddler}          {totalToddlerCost:.2f}")
    print("")
    print("Total cost ============> $",totalCostForAll)
    print("")
    print("Enjoy your stay at Disneyland, the happiest place on earth!")

def get_guest_type(guestAge):
        if guestAge >= 0 and guestAge <= 2:
            return 't'
        elif guestAge >= 3 and guestAge <= 9:
            return 'c'
        else:
            return 'a'




    
    
    
    
    
    
main()
    

















