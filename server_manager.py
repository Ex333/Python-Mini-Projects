
def show_menu():
    print("*"*30)
    print("1. Add server")
    print("2. Show servers")
    print("3. Check server")
    print("4. Exit")
    print("*"*30)

def add_server():
    name = input("Add server name: ")
    ip = input("Add IP address: ")
    os = input("Add operating system: ")
    status = input("Add status: ")

    server = {
        name: {
            "ip": ip,
            "os": os,
            "status": status
        }
    }

    servers.append(server)

def show_servers():
    for server in servers:
        print("*"*30)
        print(server)
        print("*"*30)

def check_server():
    for server in servers:
        for name, info in server.items():

            if info["status"].lower() == "online":
                print("*" * 20)
                print(f"{name} -> ONLINE")
                print("*" * 20)

            elif info["status"].lower() == "offline":
                print("*" * 20)
                print(f"{name} -> OFFLINE")
                print("*" * 20)

            else:
                print(f"{name} -> UNKNOWN STATUS")





servers =[]

while True:
    show_menu()
    choice = input("Give me your choice 1-4: \n")
    if choice == "1" or choice.lower() == "add server":
        add_server()
    elif choice == "2" or choice.lower() == "show servers":
        show_servers()
    elif choice == "3" or choice.lower() == "check server":
        check_server()
    elif choice == "4" or choice.lower() == "exit":
        break
    else:
        print("*"*30)
        print("Wrong value Try again!!")
        input("Press enter to continue.... ")
        print("*"*30)