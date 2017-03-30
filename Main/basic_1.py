import pandas as pd
import matplotlib.pyplot as plt



def read_csv(file_name):
    data = pd.read_csv(file_name, error_bad_lines=False)
    data = data[data["Region"].isin(["E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006", "E12000007", "E12000008", "E12000009", "W92000004"])]
    data = data[data["Residence Type"].isin(['C', 'H'])]
    data = data[data["Family Composition"].isin([1, 2, 3, 4, 5, 6, -9])]# can change to: list(range(0, x).append(-9)
    data = data[data["Population Base"].isin([1, 2, 3])]
    data = data[data["Sex"].isin([1, 2])]
    data = data[data["Age"].isin([1, 2, 3, 4, 5, 6, 7, 8])]
    data = data[data["Marital Status"].isin([1, 2, 3, 4, 5])]
    data = data[data["Student"].isin([1, 2])]
    data = data[data["Country of Birth"].isin([1, 2, -9])]
    data = data[data["Health"].isin([1, 2, 3, 4, 5, -9])]
    data = data[data["Ethnic Group"].isin([1, 2, 3, 4, 5, -9])]
    data = data[data["Religion"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    data = data[data["Economic Activity"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    data = data[data["Occupation"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    data = data[data["Industry"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -9])]
    data = data[data["Hours worked per week"].isin([1, 2, 3, 4, -9])]
    data = data[data["Approximated Social Grade"].isin([1, 2, 3, 4, -9])]
    data.duplicated(["Person ID"], keep="first")
    data.to_csv('refined.csv', index=False)
    print(data)




read_csv("data")