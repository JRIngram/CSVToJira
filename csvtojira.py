import csv

def convertStringToJiraRow(csvRow):
    convertedRow = "|" + csvRow.replace(",",  "|") + "|"
    return convertedRow
    
def convertStringToJiraHeader(csvRow):
    convertedRow = "||" + csvRow.replace(",",  "||") + "||"
    return convertedRow


def convertCSVFileToJira():
    with open("test.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        firstRow = True
        convertedString = ""
        for row in reader:
            if(firstRow):
                originalString = row[0] + ',' + row[1] + ',' + row[2]
                convertedString = convertStringToJiraHeader(originalString) + "\n"
                firstRow = False
                
            else:
                originalString = row[0] + ',' + row[1] + ',' + row[2]
                convertedString = convertedString + convertStringToJiraRow(originalString) + "\n"
                
        print(convertedString)
        file = open("test.txt",  "w")
        file.write(convertedString)
        file.close()

convertCSVFileToJira()
print("Conversion completed!")
