import pandas as pd

def inner_merge_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df1      \n{df1}")


    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df2      \n{df2}")

    mdf = df1.merge(df2)
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='subjects', how = 'inner')
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='dtype', how = 'inner')
    print(f"mdf      \n{mdf}")

def left_merge_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df2      \n{df2}")

    mdf = df1.merge(df2)
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='subjects', how = 'left')
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='dtype', how = 'left')
    print(f"mdf      \n{mdf}")

def right_merge_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df2      \n{df2}")

    mdf = df1.merge(df2)
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='subjects', how = 'right')
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='dtype', how = 'right')
    print(f"mdf      \n{mdf}")

def outer_merge_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}) 
    print(f"df2      \n{df2}")

    mdf = df1.merge(df2)
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='subjects', how = 'outer')
    print(f"mdf      \n{mdf}")

    mdf = df1.merge(df2, on='dtype', how = 'outer')
    print(f"mdf      \n{mdf}")

def inner_join_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index = ["s1", "s2", "s3"]) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index=['s2', 's3', 's4']) 
    print(f"df2      \n{df2}")

    # jdf = df1.join(df2, how = 'inner')
    jdf = df1.join(df2, how = 'inner',  on='dtype', lsuffix='_left', rsuffix='_right')
    print(f"jdf      \n{jdf}")

def left_join_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index = ["s1", "s2", "s3"]) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index=['s2', 's3', 's4']) 
    print(f"df2      \n{df2}")

    # jdf = df1.join(df2, how = 'inner')
    jdf = df1.join(df2, how = 'left',  on='dtype', lsuffix='_left', rsuffix='_right')
    print(f"jdf      \n{jdf}")

def right_join_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index = ["s1", "s2", "s3"]) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index=['s2', 's3', 's4']) 
    print(f"df2      \n{df2}")

    # jdf = df1.join(df2, how = 'inner')
    jdf = df1.join(df2, how = 'right',  on='dtype', lsuffix='_left', rsuffix='_right')
    print(f"jdf      \n{jdf}")

def outer_join_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index = ["s1", "s2", "s3"]) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index=['s2', 's3', 's4']) 
    print(f"df2      \n{df2}")

    # jdf = df1.join(df2, how = 'inner')
    jdf = df1.join(df2, how = 'outer',  on='dtype', lsuffix='_left', rsuffix='_right')
    print(f"jdf      \n{jdf}")

def concatinate_dataframes():
    subjects = ['Python', 'C', 'R']
    dtype = ['Scripting', 'Language', 'Scientific']
    books = [100, 200, 300]
    
    df1 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index = ["s1", "s2", "s3"]) 
    print(f"df1      \n{df1}")

    subjects = ['C++', 'C', 'OS']
    dtype = ['Programming', 'Language', 'Operating System']
    books = [500, 600, 700]
    
    df2 = pd.DataFrame({'subjects': subjects, 'dtype': dtype, 'books': books}, index=['s2', 's3', 's4']) 
    print(f"df2      \n{df2}")

    cdf = pd.concat([df1, df2])
    print(f"cdf      \n{cdf}")
    

    
def main():
    # inner_merge_dataframes()
    # left_merge_dataframes()
    # right_merge_dataframes()
    # outer_merge_dataframes()
    
    # inner_join_dataframes()
    # left_join_dataframes()
    # right_join_dataframes()
    # outer_join_dataframes()
    
    concatinate_dataframes()
    pass

if __name__ == "__main__":
    main()
