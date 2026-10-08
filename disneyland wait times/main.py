

anotherRide = ""
anotherRideName = ""


rides = ["Pirates of the Caribbean",
         "Haunted Mansion", 
         "Space Mountain", 
         "The Matterhorn",
         "Big Thunder Mountain Railroad",
         "Autopia",
         "Millennium Falcon",
         "Rise of the Resistance",
         "Snow White's Enchanted Wish",
         "Peter Pan's Flight"]
waitTimes = [15, 13, 60, 45, 35, 25, 45, 85, 40, 45]

anotherRide = input("Welcome to Disneyland! Enter another ride? (y/n): ")

while anotherRide.lower() == "y":
    anotherRideName = input("Enter ride name:")
    waitTime = int(input(f"Enter wait time for {anotherRideName}: "))
    
    
    waitTimes.append(waitTime)
    rides.append(anotherRideName)
    anotherRide = input("Enter another ride? (y/n): ")
    

totalwait = 0
average = 0
lowest_index = 0
highest_index = 0



print()
print(f"{'RIDE':35}WAIT TIME (MIN)")
print("---------------------------------------------------")
for i in range(len(rides)):
    print(f"{rides[i]:35} {waitTimes[i]}")
    totalwait += waitTimes[i]
    if waitTimes[i] < waitTimes[lowest_index]:
        lowest_index = i
    if waitTimes[i] > waitTimes[highest_index]:
        highest_index = i

average = totalwait / len(waitTimes)
averageInt = int(average)
print(f"Average wait time for all rides: {averageInt} minutes")


print(f"{rides[lowest_index]} has the shortest wait time at only {waitTimes[lowest_index]} minutes.")
print(f"{rides[highest_index]} has the longest wait time at {waitTimes[highest_index]} minutes.")
print("Enjoy your stay at Disneyland, the happiest place on earth!")





























