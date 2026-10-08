user_choice = 0
str_size = ""
str_protein = ""
str_veg = ""
base_cost = 0
protein_cost = 0
veg_cost = 0
total_cost = 0
user_choice_protein = 0
user_choice_veg = 0

print("Welcome to Pizza Express!")
print("Please use our Pizza Wizard app to place your order in three easy steps.")
print("Let's Begin!")
print("")
print("Step 1: Choose your pizza size:")
print("")
print("1) 6-inch (Personal) - $6.95\n2) 12-inch (Dinner for Two) - $12.95\n3) 18-inch (Family-Sized) - $19.95")
print("")
user_choice = int(input("Enter your option (1-3) =======> "))
print("")
print("Step 2: Choose your protein:")
print("")
print("1) Sausage - $2.95\n2) Pepperoni - $1.95\n3) Diced Tofu - $2.95")
user_choice_protein = int(input("Enter your option (1-3) =======> "))
print("")
print("Step 3: Choose your vegetable:")
print("")
print("1) Green Pepper - $1.50\n2) Mushrooms - $.50\n3) Black Truffle - $14.95")
user_choice_veg = int(input("Enter your option (1-3) =======> "))
print("")
print("PIZZA EXPRESS ORDER CONFIRMATION\n--------------------------------")
if user_choice == 1:
    print("$6.95\t6-inch (Personal)")
    str_size = "6-inch (Personal)"
    base_cost = 6.95
elif user_choice == 2:
       print("12.95\t12-inch (Dinner for Two)")
       str_size = "12-inch (Dinner for Two)"
       base_cost = 12.95
else: 
    print("$19.95\t18-inch (Family-Sized)")
    str_size = "18-inch (Family-Sized)"
    base_cost = 19.95
    
if user_choice_protein == 1:
    print("$2.95\tSausage")
    str_protein = "Sausage"
    protein_cost = 2.95
elif user_choice_protein == 2:
       print("1.95\tPepperoni")
       str_protein = "Pepperoni"
       protein_cost = 1.95
else: 
    print("$2.95\tDiced Tofu")
    str_protein = "Diced Tofu"
    protein_cost = 2.95

if user_choice_veg == 1:
    print("$1.50\tGreen Pepper")
    str_veg = "Green Pepper"
    veg_cost = 1.50
elif user_choice_veg == 2:
       print("0.50\tMushrooms")
       str_veg = "Mushrooms"
       veg_cost = 0.50
else: 
    print("$14.95\tBlack Truffle")
    str_veg = "Black Truffle"
    veg_cost = 14.95
   
total_cost = base_cost + protein_cost + veg_cost
print("")
print(f"Total:${total_cost:.2f}")
print("Thank You for Your Order!")

    
    
    
    
    
    
