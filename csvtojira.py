import csv

def convertStringToJiraRow(csvRow):
    convertedRow = "|" + csvRow.replace(",",  "|") + "|\n"
    return convertedRow
    
def convertStringToJiraHeader(csvRow):
    convertedRow = "||" + csvRow.replace(",",  "||") + "||\n"
    return convertedRow 


def convertCSVStringToJira(CSVString):
    stringArray = CSVString.splitlines()
    convertedString = ""
    firstRow = True
    for line in stringArray:
        if(firstRow):
            convertedString = convertStringToJiraHeader(line)
            firstRow = False
        else:
            convertedString = convertedString + convertStringToJiraRow(line)
     
    print(convertedString)
def convertCSVFileToJira():
    with open("test.csv", 'r') as csvfile:
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
                
        print(convertedString)
        file = open("test.txt",  "w")
        file.write(convertedString)
        file.close()

convertCSVFileToJira()
print("*********************************************************************")
convertCSVStringToJira("letter,food,healthy\na,apple,Y\nb,banana,Y\nc,chocolate,N\nd,dried fruit,Y")
print("Conversion completed!")
