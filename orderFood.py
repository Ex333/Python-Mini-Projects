from art import text2art
from datetime import datetime

print(text2art("ORDER YOUR FOOD"))

#Orders Dict
orders = {}
time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

def show_menu():
       print("==============================")
       print("          MAIN MENU")
       print("==============================")
       print("1. New order")
       print("2. Show orders")
       print("3. Calculate total")
       print("4. Send confirmation")
       print("0. Exit")
       print("==============================")

def new_order():
       name =  input("Gimme  your name: \n")
       order = input("What is your order: \n ")
       quantity = int(input("Quantity: \n"))
       order_time = time

       orders[name] = {
              "order":  order,
              "quantity": quantity,
              "orde_time": order_time
       }

       input("Press enter to continue...")

def show_orders():
    for key, value in orders.items():
        print(
            f"User {key} ordered: {value['order']} "
            f"and quantity is: {value['quantity']}. "
            f"Order was confirmed at {value['orde_time']}"
        )
        input("Press enter to continue...")
    
while True:
       show_menu()
       choice = input("Choose your option:")

       if choice == "1" or choice.lower() == "new order":
              new_order()
       elif choice == "2" or choice.lower() == "show orders":
              show_orders()
       elif choice == "3" or choice.lower() == 'calculate total':
              pass
       elif choice == "4" or choice.lower() == "send confirmation":
              pass
       elif choice == "0" or choice.lower() == "exit":
              pass
       else:
              print("Invalid value")
