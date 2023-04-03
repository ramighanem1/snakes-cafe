menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

def Welcome():
   print('**************************************')
   print('**    Welcome to the Snakes Cafe!   **')
   print('**    Please see our menu below.    **')
   print("**                                  **")
   print('** To quit at any time, type "quit" **')
   print('**************************************')

def Menu():
    """
    Prints out all items on the Menu
    """
    for group, items in menu.items():
        print('')
        print(group)
        print('----------')
        for item in items:
            print(item)
        print('')

def Allitem():
    ListItem = []
    for items in menu.values():
        for item in items:
            ListItem.append(item.lower())
    return ListItem

def MyOrder(orders):
    print('')
    for item, quantity in orders.items():
        if(quantity==1):
            print(f"** {quantity} order of {item.capitalize()} have been added to your meal **")
        else:
            print(f"** {quantity} orders of {item.capitalize()} have been added to your meal **")
    print('')

def Order():
    orders = {}
    while True:
        print('**************************************')
        print('** What would you like to order? **')
        print('**************************************')
        order = input("> ")
        order = order.lower()
        if order == "quit":
            break
        elif order in orders:
            orders[order] += 1
        elif order in Allitem():
            orders[order] = 1
        else:
            print(order + " is not exist on the menu \n")
        MyOrder(orders)



if __name__ == '__main__':
  Welcome()
  Menu()
  Order()
  