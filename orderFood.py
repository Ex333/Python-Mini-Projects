from art import text2art


print(text2art("ORDER YOUR FOOD"))

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


while True:
       show_menu()
       choice = input("Choose your option:")

       if choice == "1" or choice.lower() == "new order":
              pass
       elif choice == "2" or choice.lower() == "show orders":
              pass
       elif choice == "3" or choice.lower() == 'calculate total':
              pass
       elif choice == "4" or choice.lower() == "send confirmation":
              pass
       elif choice == "0" or choice.lower() == "exit":
              pass
       else:
              print("Invalid value")
