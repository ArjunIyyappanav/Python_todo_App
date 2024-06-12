import FreeSimpleGUI as fsg
from functions import get,writetodo,complete
label = fsg.Text("Enter a to-do")
buttonadd = fsg.Button("Add")
buttonedit = fsg.Button("Edit")
buttoncomplete = fsg.Button("Complete")
inputtext = fsg.InputText(tooltip = "Enter todo",key="todo")
list_box = fsg.Listbox(values = get(),key = "todos",enable_events = True,size = [45,10])

window = fsg.Window("My to-do app",layout =[[label],[inputtext,buttonadd],[list_box],[buttonedit,buttoncomplete]],sbar_arrow_width=(14),font = ("Helvetica",16))
while True:
    event,values = window.read()
    match event:
        case 'Add':
            if(values['todo'] != ''):
                content = values['todo']+"\n"
                writetodo(content)
                window['todos'].update(values = get())
            else:
                fsg.popup("Enter an activity to Add!!",font = ('Helvetica',14))
                #window['todo'].update(value = "Enter an activity to Add!!",font = (14))
        case 'Edit':
            try:
                content = get()
                new_todo = values['todo']
                content[content.index(values['todos'][0])] = new_todo+'\n'
                filehandler =  open("todos.txt",'w') 
                filehandler.writelines(content)
                filehandler.close()
                window['todos'].update(values = get())
            except IndexError:
                fsg.popup("Choose an activity to Edit!!",font = ('Helvetica',14))
        
        case 'Complete':
            try:
                complete(values['todos'][0])
                window['todos'].update(values = get())
                window['todo'].update(value = '')
            except IndexError:
                fsg.popup("Choose an activity to Complete!!",font = ('Helvetica',14))
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case fsg.WIN_CLOSED:
            break

window.close()

