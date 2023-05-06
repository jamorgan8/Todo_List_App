while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

# match function literally attempts to match what is input to the specified variable. Similar to case/when in SQL
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n" # "\n" is a line break

            # open function creates a file object. open function takes 2 arguments- the file path and a character
            # code (r, a, w, x).
            # This chunk of code opens and saves the contents of the text file as a list then closes the file.
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close() # close file object to make sure other aspects of code don't interact

            # Adds the new entry to list
            todos.append(todo)

            # opens text file again and replaces contents with new list which is the original contents plus the addition
            file = open('todos.txt', 'w')
            # method for file objects. Takes 1 argument which must be a list
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(new_todos): # iterates over todos list and prints index + 1 and item
                item = item.strip('\n')
                print(f"{index+1}- {item}") #f string prints literal string as defined inside quotes

        case 'edit':
            number = int(input("Enter number of todo to edit: ")) ## int converts str.
            number = number - 1 # to correct for the python index starting at 0
            new_todo = input("Enter new todo: ") ## stores new item
            todos[number] = new_todo # stores new item to todos list at location of original

        case 'complete':
            number = int(input("Enter number of todo to complete: "))
            removed = todos.pop(number-1)
            print('Great work! You finished: ', removed)

        case 'exit':
            break # breaks while loop

print("Bye!")


