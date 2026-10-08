



class MenuItem:
    
    def __init__(self, itemName:str, category:str, price:float, calories:int, hasNuts:bool, sellBy:str):
        self.itemName = itemName
        self.category = category
        self.price = price
        self.calories = calories
        self.hasNuts = hasNuts
        self.sellBy = sellBy
        
    def print_menu_item(self):
        if self.hasNuts:
            YesNo = "yes"
        else:
            YesNo = "no"
            
        print(f"\nFrom our exclusive {self.category} collection")
        print("-----------------------------------------------------")
        print(f"{self.itemName}")
        print(f"Today's special price: ${self.price:.2f}")
        print(f"Calories: {self.calories}")
        print(f"Contains nuts: {YesNo}")
        print(f"Freshness guarantee through: {self.sellBy}")
        
def main(): 
    Tomorrow = "July 22, 2024."
    items = []
    items.append(MenuItem("Caffe Americano", "coffee", 4.95, 0, False, "eternity"))
    items.append(MenuItem("Flat White", "coffee", 5.95, 80, False, "eternity"))
    items.append(MenuItem("Green Machine", "smoothie", 7.95, 250, False, "eternity"))
    items.append(MenuItem("Cranberry-Pistachio Scone", "pastry", 3.50, 300, True, Tomorrow))
    items.append(MenuItem("Chocolate Chip Scone", "pastry", 3.50, 275, False, Tomorrow))

    for item in items:
        item.print_menu_item()
















main()
































