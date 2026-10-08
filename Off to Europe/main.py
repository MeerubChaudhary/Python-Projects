dollars = 0
euros = 0
tempF = 0
tempC = 0
lbsChoc = 0
kgChoc = 0
DOLLARS_TO_EUROS = 0.94
dressMessage = ""

dollars = float(input("How many U.S. dollars can you afford to spend on your trip?: "))
lbsChoc = float(input("How many pounds of chocolate will you be buying?: "))
tempC = float(input("What is the temperature in degrees C on the European news?: "))
print("ITINERARY NOTES")
print("")
print("------------------------------------------------------------------")
print("")
euros = dollars * DOLLARS_TO_EUROS
print("You have ",f"{euros:.2f}" , "Euros to spend.")
print("")
kgChoc = lbsChoc / 2.2
print("Plan to buy", f"{kgChoc:.2f}" , "Kg of chocolate for family and friends.")
print("")
tempF = tempC * 9 / 5 + 32
if tempF < 50:
    print("The temperature in Europe is", f"{tempF:.2f}" , "degrees F, so bundle up.")
elif tempF > 70:
    print("The temperature in Europe is", f"{tempF:.2f}" , "degrees F, so dress coolly.")
else: 
    print("The temperature in Europe is", f"{tempF:.2f}" , "degrees F, so bring a light jacket.")
 
print("")   
print("Bon Voyage!")