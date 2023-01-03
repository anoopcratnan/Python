todos = []
while True:
    user_action = input("Type add,show,edit, exit :")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Enter thr number of todo to edit : "))
            number = number - 1
            new_todo = input("Enter new to do :")
            todos[number] = new_todo
        case 'exit':
            break
print("bye")



