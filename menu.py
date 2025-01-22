# restaurant-menu-app
def_init_(self):
 self.menu_items = {}

def add_item(self, name, price):
 self.menu_items[name] = price

def get_price(self, name):
 return self.menu_items.get(name, None)
def update_price(self, name, new_price):
       if name in self.menu_items:
          self.menu_items[name] = new_price
          return True
       return False      

def main():
menu = RestaurantMenu()
#Add initital menu items
menu.add_item("Burger", 10.99)
menu.add_item("Fries, 4.99)

if_name_ == "_main_":
main()
