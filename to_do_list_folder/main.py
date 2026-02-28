while True:
    answer = input('Do you want to add a new To-Do item? (y/n) or type "exit": ').lower()

    if answer == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    elif answer == "y":
        item = input("Enter your new To-Do item: ")

        file = open("to_do.txt", "a")
        file.write(item + "\n")
        file.close()

    elif answer == "n":
        read_answer = input('Do you want to list your To-Do items? (y/n): ').lower()

        if read_answer == "y":
            file = open("to_do.txt", "r")
            content = file.read()
            print("\nYour To-Do List:")
            print(content)
            file.close()

    else:
        print("Invalid input")
        