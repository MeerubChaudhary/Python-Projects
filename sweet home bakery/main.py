





def main():
    halve_recipe(1,.75,2)
    print(f"A one-tier cake with a 20-inch diameter will serve {calc_slices(20):.0f} guests.")
    print(f"A two-tier cake with a 20- and 16-inch diameters will serve {calc_slices(20, 16):.0f} guests.")
    print(f"A three-tier cake with a 20-, 16-, and 12-inch diameters will serve {calc_slices(20,16,12):.0f} guests.")
    
def halve_recipe(butter, sugar, flour):
    half_butter = butter/2
    half_sugar = sugar/2
    half_flour = flour/2
    print("Half Batch Shortbread Recipe")
    print("-----------------------------")
    print(half_butter, "\tC Butter")
    print(half_sugar, "\tC Sugar")
    print(half_flour, "\tC Flour")
    print("")

def calc_slices(diam1, diam2=0, diam3=0):
    surfacearea1 = (3.14 * (diam1/2)**2)
    surfacearea2 = (3.14 * (diam2/2)**2)
    surfacearea3 = (3.14 * (diam3/2)**2)
    totalsurfacearea = surfacearea1 + surfacearea2 + surfacearea3
    numSlices = totalsurfacearea / 7.34
    return numSlices
    
    
    
main()












