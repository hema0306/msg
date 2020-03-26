import pandas


data = [

     ['India', 1_351.16, 3_287.26, 2_575.67, 'Asia', '1947-08-15'],
     ['China', 1_398.72, 9_596.96, 12_234.78, 'Asia'],
     ['US', 329.74, 9_833.52, 19_485.39, 'N.America', '1776-07-04'],
     ['Indonesia', 268.07, 1_910.93, 1_015.54, 'Asia', '1945-08-17'],
     ['Brazil', 210.32, 8_515.77, 2_055.51, 'S.America', '1822-09-07']

      ]

#converts data into dataframe
df = pandas.DataFrame(data = data, columns = ['COUNTRY', 'POP', 'AREA', 'GDP', 'CONT', 'IND_DAY']).T
# print(df)

#imports data to csv file
csv_data = df.to_csv('listcsvfile.csv')

#reads data from csv files
read_csv = pandas.read_csv('listcsvfile.csv', skiprows=range(2,10,2))
print(read_csv)

#imports data to json file
json_data = df.to_json('listjsonfile.json')

#below code produces one large dictionary with the column labels as
#keys and the corresponding inner dictionaries as values
column_json = df.to_json('listjsonfile-columns.json')

#this produces json file which holds a list with one dictionary for each row
record_json = df.to_json('listjsonfile-records.json', orient = 'records')

#this produces json file contains one dictionary that holds following lists
#names of columns
#labels of rows
#inner lists(2D sequence) that holds data values
record_json = df.to_json('listjsonfile-split.json', orient = 'split')

#imports data to excel
excel_data = df.to_excel('listdata.xlsx')

#this produces excel with sheet name as specified and will start at 3rd row and 5th column as specified
excel_data = df.to_excel('listdata-shifted.xlsx', sheet_name='COUNTRIES', startrow=2, startcol=4)

#reads data from excel
read_excel = pandas.read_excel('listdata.xlsx')
print(read_excel)