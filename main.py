## initialize empty list
todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

## match function literally attempts to match what is input to the specified variable. Similar to case/when in SQL
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show':
            for index, item in enumerate(todos): # iterates over todos list and prints index + 1 and item
                print(f"{index+1}- {item}") #f string prints literal string as defined inside quotes

        case 'edit':
            number = int(input("Enter number of todo to edit: ")) ## int converts str.
            number = number - 1 ## to correct for the python index starting at 0
            new_todo = input("Enter new todo: ") ## stores new item
            todos[number] = new_todo ## stores new item to todos list at location of original

        case 'complete':
            number = int(input("Enter number of todo to complete: "))
            removed = todos.pop(number-1)
            print('Great work! You finished: ', removed)

        case 'exit':
            break ##breaks while loop

print("Bye!")


