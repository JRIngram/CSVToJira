import tkinter

def activateConvertButton(conversion):
    if conversion == "File":
        print("FILE")
    elif type == "Text":
        print("TEXT")

def createGUI():
    window = tkinter.Tk()
    window.title("CSV To Jira")

    #The button which when pressed converts text.
    convertButton = tkinter.Button(window,  text="Convert",  state="disabled").grid(row=2,  column=3)
    


    conversionFromLabel = tkinter.Label(window,  text="Convert from a CSV File or Text Input Below?:").grid(row=0)
    conversionFrom = ""
    textEnteredRadio = tkinter.Radiobutton(window, text="Text Entered Below", variable=conversionFrom, value="Text").grid(row=0,  column=1)
    csvFileRadio = tkinter.Radiobutton(window, text="CSV File", variable=conversionFrom, value="File", command=lambda: activateConvertButton("File")).grid(row=0,  column=2)


    textArea = tkinter.Text(window, width=80, height=30).grid(row=1, columnspan=3)

    window.mainloop()

createGUI()
