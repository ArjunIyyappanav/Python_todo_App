filepath = "todos.txt"

def get(file=filepath):
    with open(file,'r') as filehandler:
        content = filehandler.readlines()
    return content
def write(content,file=filepath):
    with open(file,'a') as filehandler:
        filehandler.write(content)
'''def edit(file=filepath):
    with open(file,'w'):'''
