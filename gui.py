import tkinter
from tkinter import filedialog
import csvtojira

def loadCSVTextToGUI(textArea):
    filePath = filedialog.askopenfilename(filetypes = (("CSV Files", "*.csv"), ("Text Files", "*.txt")))
    textArea.insert('1.0',  csvtojira.convertCSVToString(filePath))

def activateConvertButton(button):
    button.config(state="normal")
    
def activateConvertAndFileDialog(button,  textArea):
    activateConvertButton(button,)
    print(loadCSVTextToGUI(textArea))
    
def convertTextToJira(textArea):
    textToConvert = textArea.get("1.0",'end-1c')
    convertedText = csvtojira.convertCSVStringToJira(textToConvert,  False)
    textArea.delete('1.0',  'end-1c')
    textArea.insert('1.0',  convertedText)

    
def createGUI():
    window = tkinter.Tk()
    window.title("CSV To Jira")

    #The button which when pressed converts text.
    #Set to a disabled state to ensure an option is selected by the radio buttons.
    convertButton = tkinter.Button(window,  text="Convert",  state="disabled",  command=lambda: convertTextToJira(textArea))
    convertButton.grid(row=2,  column=2)
    

    conversionFrom = ""
    conversionFromLabel = tkinter.Label(window,  text="Convert from a CSV File or Text Input Below?:")
    conversionFromLabel.grid(row=0)
    
    #Creates two radio buttons for options on what to convert from.
    textEnteredRadio = tkinter.Radiobutton(window, text="Text Entered Below", variable=conversionFrom, value="Text", command=lambda: activateConvertButton(convertButton))
    textEnteredRadio.grid(row=0,  column=1)
    csvFileRadio = tkinter.Radiobutton(window, text="CSV File", variable=conversionFrom, value="File", command=lambda: activateConvertAndFileDialog(convertButton,  textArea))
    csvFileRadio.grid(row=0,  column=2)


    textArea = tkinter.Text(window, width=80, height=30)
    textArea.grid(row=1, columnspan=4)

    window.mainloop()


createGUI()
