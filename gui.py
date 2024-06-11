import FreeSimpleGUI as fsg
label = fsg.Text("Enter a to-do")
buttonadd = fsg.Button("Add")
inputtext = fsg.InputText(tooltip = "Enter todo")
window = fsg.Window("My to-do app",layout = [[label],[inputtext,buttonadd]])
window.read() 
window.close()

