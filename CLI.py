from functions import get,writetodo,complete
file = open('todos.txt','w')
file.close()
while True:
    user_input = input("Enter Action : ").split(" ",1)
    match user_input[0].lower():
        case 'add':
            writetodo(user_input[1]+'\n')
        case 'show':
             for no,todo in enumerate(get()):
                 todo = todo.strip("\n")
                 print(f"{no+1}-{todo}")
        case 'complete':
            complete(user_input[1].lower()+'\n')
        case 'edit':
            content = get()
            for i in content:
                if user_input[1].lower() == i.strip('\n'):
                    new_input = input("Enter New to-do : ")
                    content[content.index(i)] = new_input+'\n'
                    with open("todos.txt","w") as filehandler:
                        filehandler.writelines(content)
        case "exit":
            print('Bye!')
            break
        case _:
            print("Enter valid to-dos")
             


