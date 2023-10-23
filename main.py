import csv

file_list = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
output_data = [["Sales", "Date", "region"]]
for file in file_list:
    with open(file) as csv_file:
        salesDayreader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in salesDayreader:
            if row[0] == "pink morsel":
                output_data.append([str(float(row[1][1:]) * int(row[2])), row[3], row[4]])

with open('data/Pink_sales_data.csv','w') as out_file:
    out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for data in output_data:
        out_writer.writerow(data)
