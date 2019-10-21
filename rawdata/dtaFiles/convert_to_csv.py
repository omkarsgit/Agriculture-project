import pandas as pd
fileno = 1959
dtaext = '.dta'
csvext = '.csv'
filename = '/Users/omkar/Desktop/GithubProjects/Agriculture-project/rawdata/csvFiles/'
while fileno <= 1987: 
    data_file = str(fileno) + dtaext
    data = pd.io.stata.read_stata(data_file)
    data.to_csv(filename + str(fileno) + csvext)
    print('Created csv file: ' + str(fileno))
    fileno+=1

print("Completed")


