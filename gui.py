import tkinter
from tkinter import filedialog
import csvtojira

def openFileDialog():
    return filedialog.askopenfilename(filetypes = (("CSV Files", "*.csv"), ("Text Files", "*.txt")))

def activateConvertButton(button):
    button.config(state="normal")
    
def activateConvertAndFileDialog(button):
    activateConvertButton(button)
    return openFileDialog()

def createGUI():
    window = tkinter.Tk()
    window.title("CSV To Jira")

    #The button which when pressed converts text.
    #Set to a disabled state to ensure an option is selected by the radio buttons.
    convertButton = tkinter.Button(window,  text="Convert",  state="disabled")
    convertButton.grid(row=2,  column=2)
    

    conversionFrom = ""
    conversionFromLabel = tkinter.Label(window,  text="Convert from a CSV File or Text Input Below?:")
    conversionFromLabel.grid(row=0)
    
    #Creates two radio buttons for options on what to convert from.
    textEnteredRadio = tkinter.Radiobutton(window, text="Text Entered Below", variable=conversionFrom, value="Text", command=lambda: activateConvertButton(convertButton))
    textEnteredRadio.grid(row=0,  column=1)
    csvFileRadio = tkinter.Radiobutton(window, text="CSV File", variable=conversionFrom, value="File", command=lambda: activateConvertAndFileDialog(convertButton))
    csvFileRadio.grid(row=0,  column=2)


    textArea = tkinter.Text(window, width=80, height=30)
    textArea.grid(row=1, columnspan=4)

    window.mainloop()


createGUI()
