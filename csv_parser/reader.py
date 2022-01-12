import csv

with open('bnkAcct.csv') as csv_file:

    print(f'Hi')

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if not row[4]:
                print(f' Income  ------ Date: \t{row[1]} ; Description: {row[2]} ; Amount Credit: {row[5]}')
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            else:
                print(f' Expense ------ Date: \t{row[1]} ; Description: {row[2]} ; Amount Debit: {row[4]}')
            line_count += 1
    print(f'Processed {line_count} lines.')