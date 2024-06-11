from functions import get,write
file = open('todos.txt','w')
file.close()
while True:
    user_input = input("Enter Action : ").split(" ",1)
    match user_input[0].lower():
        case 'add':
            write(user_input[1]+'\n')
        case 'show':
             for no,todo in enumerate(get()):
                 todo = todo.strip("\n")
                 print(f"{no+1}-{todo}")
        #case 'edit':
             


