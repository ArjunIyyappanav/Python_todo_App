import webbrowser
user_input = input("Enter Search item : ").replace(" ","+")
webbrowser.open("https://google.com/search?q="+user_input)