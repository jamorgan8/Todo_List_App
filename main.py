while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

# match function literally attempts to match what is input to the specified variable. Similar to case/when in SQL
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n" # "\n" is a line break

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Adds the new entry to list
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos): # iterates over todos list and prints index + 1 and item
                item = item.strip('\n')
                print(f"{index+1}- {item}") #f string prints literal string as defined inside quotes

        case 'edit':
            number = int(input("Enter number of todo to edit: ")) ## int converts str.
            number = number - 1 # to correct for the python index starting at 0

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ") ## stores new item
            todos[number] = new_todo + '\n' # stores new item to todos list at location of original

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter number of todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from your list. Great work!"
            print(message)

        case 'exit':
            break # breaks while loop

print("Bye!")


