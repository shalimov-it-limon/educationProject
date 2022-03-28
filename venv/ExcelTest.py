import pandas as pd
import  xlsxwriter

# Specify a writer
writer = pd.ExcelWriter('E:\Work\\result.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file
list ={'col1':['num','name','url'],'col2':[1,'some name','some url']}
yourData = pd.DataFrame(list)
yourData.to_excel(writer, 'Sheet1')

# Save the result
writer.save()