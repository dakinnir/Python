#importimg necessary file
import pandas as pd

#path for the excel file
xl_path = '/Users/danielakinniranye/Documents/Project/Excel/SampleData.xlsx'
data_sheet = pd.read_excel(xl_path, sheet_name='SalesOrders') #passing in the proper sheet name
#print(content)

#      group total sum by the item
#only the unique values in the sheet column named 'Item'
by_item = data_sheet['Item'].unique()
#print(by_item)


#creating new excel for the different group of items
for order in by_item:
    #using the first data frame
    new_data_sheet = data_sheet[data_sheet['Item'] == order ]
    #our new excel file name
    new_file = "Item-" + str(order) + '-Order.xlsx'
    new_data_sheet.to_excel(new_file, index=False)
