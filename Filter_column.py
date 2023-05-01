import pandas as pd

inputFileName = input("Enter name of input file: ")

# reading the CSV file
csvFile = pd.read_csv(inputFileName,header =0, usecols=[ "Year", "Units"])

# displaying the contents of the CSV file & display the read CSV data 
#print(csvFile)


# replacing blank spaces with '_'
csvFile.columns =[column.replace(" ", "_") for column in csvFile.columns]

# filtering with query method
csvFile.query('Year == 2021',inplace=True)
# display
csvFile

