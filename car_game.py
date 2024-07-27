is_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if is_started:
            print("The car already started")
        else:
            print("The car started")
            is_started = True
    elif command == "stop":
        if not is_started:
            print("The car already stopped")
        else:
            print("The car stopped")
            is_started = False
    elif command == "help":
        print("""
start - To start the car
stop  - To stop the car
quit  - To quit the program 
""")
    elif command == "quit":
        break
    else:
        print("Sorry! I don't understand what you want.")
