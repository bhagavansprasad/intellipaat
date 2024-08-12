import pandas as pd

def dump_dataframe_by_worksheet(wbook, wsheet):
    wb = pd.ExcelFile(wbook)
    ws = wb.parse(wsheet)
    
    print(ws)
    
    wb.close()   
    print()
    

def print_all_worksheet_names(wbname):
    wb = pd.ExcelFile(wbname)

    print(wb.sheet_names)

    for wsheet in wb.sheet_names:
        print(wsheet)
        
    wb.close()
    print ("")

def print_cell_values(wbname, worksheet):
    wb = pd.ExcelFile(wbname)
    ws = wb.parse(worksheet)
    
    # print(data.max())
    print(ws.shape)
    rcount, ccount = ws.shape
    print(f"max rows filled :{rcount}")
    print(f"max cols filled :{ccount}")
    print(ws.columns)

    print(f"wsheet[1, 0] :{ws.iloc[1, 0]}") 
    print(f"wsheet[3, 1] :{ws.iloc[3, 1]}") 
    print()
    return

def mean_by_column_name(wbname, worksheet, columnname):
    wb = pd.ExcelFile(wbname)
    ws = wb.parse(worksheet)
    
    meanv = ws[columnname].mean()
    print(f"mean value of {columnname} :{meanv}")
    print()
 
    wb.close()

def mode_by_column_name(wbname, worksheet, column_name):
    wb = pd.ExcelFile(wbname)
    ws = wb.parse(worksheet)
    
    modev = ws[column_name].mode()
    print(f"mode :\n{modev}")
    print()

    wb.close()

def standard_deviation_by_column_name(wbname, worksheet, column_name):
    wb = pd.ExcelFile(wbname)
    ws = wb.parse(worksheet)
    
    
    stdv = ws[column_name].std()
    print(f"std deviation of column {column_name} is :{stdv}")

    wb.close()
    print()

def range_by_column_name(wbname, worksheet):
    wb = pd.ExcelFile(wbname)
    ws = wb.parse(worksheet)
    
    
    range_x = ws['x'].max() - ws['x'].min()
    range_y = ws['y'].max() - ws['y'].min()
    
    print(f"range_x :{range_x}")
    print(f"range_y :{range_y}")

    wb.close()
    print()

def main():
    filename = "data.xlsx"
    wsheet_name = "datasheet1"

    dump_dataframe_by_worksheet(filename, wsheet_name)
    mean_by_column_name(filename, wsheet_name, 'x')
    mean_by_column_name(filename, wsheet_name, 'y')

    mode_by_column_name(filename, wsheet_name, 'x')
    mode_by_column_name(filename, wsheet_name, 'y')

    standard_deviation_by_column_name(filename, wsheet_name, 'x')
    standard_deviation_by_column_name(filename, wsheet_name, 'y')
   
    range_by_column_name(filename, wsheet_name)
    return

if (__name__ == '__main__'):
    main()

[42 61 39 70 8 30 52 28 95 86 35 77 80 86 1 84 90 57 45 6 1 56 60 83 24 63 93 59 92 53]
