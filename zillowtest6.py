import csv

rdr = csv.reader(open(r'E:/Zillow views-saves.csv'))
line_count = 0
row_count = 0
views = 0
saves = 0
current_month = ''
for row in rdr:
    row_count += 1
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    if row_count == 2:
        current_month = {row[0]}
    if row_count >= 2:
        month = {row[0]}
        if row[2] != '':
            views += int(row[2])
            
        if row[3] != '':
            saves += int(row[3]) 
            
        if  month != current_month:
            print(f'For the month of {current_month} there were {views} and {saves} saves')
            views = 0
            saves = 0
            current_month = month    
                 
# print last total
print(f'For the month of {current_month} there were {views} and {saves} saves')


 