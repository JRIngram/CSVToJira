import csv

def convertStringToJiraRow(csvRow):
    convertedRow = "|" + csvRow.replace(",",  "|") + "|\n"
    return convertedRow
    
def convertStringToJiraHeader(csvRow):
    convertedRow = "||" + csvRow.replace(",",  "||") + "||\n"
    return convertedRow 
    
def outputToTextFile(convertedString):
    file = open("CSVToJiraOutput.txt",  "w")
    file.write(convertedString)
    file.close()

def convertCSVStringToJira(CSVString,  outputToFile):
    stringArray = CSVString.splitlines()
    convertedString = ""
    firstRow = True
    for line in stringArray:
        if(firstRow):
            convertedString = convertStringToJiraHeader(line)
            firstRow = False
        else:
            convertedString = convertedString + convertStringToJiraRow(line)
    if(outputToFile):
        outputToTextFile(convertedString)
    print(convertedString)
    
'''
Possibly unneeded?
Could load the CSV File into Text field and convert in the GUI.
'''
def convertCSVFileToJira(filePath,  outputToFile):
    with open(filePath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        firstRow = True
        convertedString = ""
        for row in reader:
            if(firstRow):
                originalString = row[0] + ',' + row[1] + ',' + row[2]
                convertedString = convertStringToJiraHeader(originalString)
                firstRow = False
                
            else:
                originalString = row[0] + ',' + row[1] + ',' + row[2]
                convertedString = convertedString + convertStringToJiraRow(originalString)
        if(outputToFile):
            outputToTextFile(convertedString)
        print(convertedString)
        
def convertCSVToString(filePath):
    with open(filePath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        outputString = ""
        for row in reader:
            outputString = outputString + str(row) + "\n"
        return outputString.replace("[",  "").replace("]",  "")

print(convertCSVToString("test.csv"))
print("*********************************************************************")
print("Converting CSV File to Jira Table")
convertCSVFileToJira("test.csv",  True)
print("*********************************************************************")
print("Converting CSV String to Jira Table")
convertCSVStringToJira("letter,food,healthy\na,apple,Y\nb,banana,Y\nc,chocolate,N\nd,dried fruit,Y",  True)
print("Conversions completed!")
