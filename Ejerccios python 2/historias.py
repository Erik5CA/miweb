pages = [
    "Page 1)Once upon a time.....\nWhat do you want to do?\nOption 1)...\nOption 2)....\nOption 3)....",
    "Page 2)Once upon a time.....\nWhat do you want to do?\nOption 1)...\nOption 2)....\nOption 3)....",
    "Page 3)Once upon a time.....\nWhat do you want to do?\nOption 1)...\nOption 2)....\nOption 3)...."
]

def showPage(pageNumber):
    text = pages[pageNumber]
    print(text)
    response = input()
    showPage(int(response))
    
showPage(0)