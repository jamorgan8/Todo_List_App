##obtain user input and save as a variable
user_prompt = "Type add, show, or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

## match literally attempts to match what is input to the specified variable. Similar to case/when in SQL
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break ##breaks while loop

print("Bye!")


