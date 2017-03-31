import pandas as pd
import matplotlib.pyplot as plt

regions = {'E12000001': 'North East', 'E12000002': 'North West', 'E12000003': 'Yorkshire and the Humber',
           'E12000004': 'East Midlands', 'E12000005': 'West Midlands', 'E12000006': 'East of England',
           'E12000007': 'London', 'E12000008': 'South East', 'E12000009': 'South West', 'W92000004': 'Wales'}

occupations = {1: "Managers, Directors and Senior Officials", 2: "Professional",
               3: "Associate Professional and Technical", 4: "Administrative and Secretarial",
               5: "Skilled Trades", 6: "Caring, Leisure and Other Service", 7: "Sales and Customer Service",
               8: "Process, Plant and Machine Operatives", 9: "Elementary", -9: "Under 16 never worked"}

ages = {1: "0 to 15", 2: "16 to 24", 3: "25 to 34", 4: "35 to 44",
        5: "45 to 54", 6: "55 to 64", 7: "65 to 74", 8: "75 and over"}

economic_acts = {1: "Employe", 2: "Self-employed", 3: "Unemployed", 4: "Full-time student",
                 5: "Retired", 6: "Student", 7: "Looking after home or family",
                 8: "Long-term sick or disabled", 9: "Other", -9: "Aged under 16 or students"}


def read_csv(file_name):
    data = pd.read_csv(file_name, error_bad_lines=False)
    data = data[data['Region'].isin(
        ['E12000001', 'E12000002', 'E12000003', 'E12000004', 'E12000005',
         'E12000006', 'E12000007', 'E12000008', 'E12000009', 'W92000004'])]
    data = data[data['Residence Type'].isin(['C', 'H'])]
    data = data[data['Family Composition'].isin([1, 2, 3, 4, 5, 6, -9])]  # can change to: list(range(0, x).append(-9)
    data = data[data['Population Base'].isin([1, 2, 3])]
    data = data[data['Sex'].isin([1, 2])]
    data = data[data['Age'].isin([1, 2, 3, 4, 5, 6, 7, 8])]
    data = data[data['Marital Status'].isin([1, 2, 3, 4, 5])]
    data = data[data['Student'].isin([1, 2])]
    data = data[data['Country of Birth'].isin([1, 2, -9])]
    data = data[data['Health'].isin([1, 2, 3, 4, 5, -9])]
    data = data[data['Ethnic Group'].isin([1, 2, 3, 4, 5, -9])]
    data = data[data['Religion'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    data = data[data['Economic Activity'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    data = data[data['Occupation'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    data = data[data['Industry'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -9])]
    data = data[data['Hours worked per week'].isin([1, 2, 3, 4, -9])]
    data = data[data['Approximated Social Grade'].isin([1, 2, 3, 4, -9])]
    data.duplicated(['Person ID'], keep='first')
    return data


def analyse(data):
    print('Total no of records: ', data.shape[0])
    print(data.groupby('Region').size(), '\n')
    print(data.groupby('Residence Type').size(), '\n')
    print(data.groupby('Family Composition').size(), '\n')
    print(data.groupby('Population Base').size(), '\n')
    print(data.groupby('Sex').size(), '\n')
    print(data.groupby('Age').size(), '\n')
    print(data.groupby('Marital Status').size(), '\n')
    print(data.groupby('Student').size(), '\n')
    print(data.groupby('Country of Birth').size(), '\n')
    print(data.groupby('Health').size(), '\n')
    print(data.groupby('Ethnic Group').size(), '\n')
    print(data.groupby('Religion').size(), '\n')
    print(data.groupby('Economic Activity').size(), '\n')
    print(data.groupby('Occupation').size(), '\n')
    print(data.groupby('Industry').size(), '\n')
    print(data.groupby('Hours worked per week').size(), '\n')
    print(data.groupby('Approximated Social Grade').size(), '\n')


def create_plot(char_type, data, column, names, title, x_axis, y_axis, legend):
    data = data.replace({column: names})
    plot = data[column].value_counts().plot(kind=char_type, title=title, legend=legend)
    plot.set_xlabel(x_axis)
    plot.set_ylabel(y_axis)
    plt.show()


d = read_csv('data')
analyse(d)
create_plot('bar', d, 'Region', regions, 'Number of Records for each region', 'Regions', 'No. of Records', True)
create_plot('bar', d, 'Occupation', occupations, 'Number of Records for each Occupation', 'Occupation', 'No. of Records', True)
create_plot('pie', d, 'Age', ages, 'Distribution of the sample by age', "", "", False)
create_plot('pie', d, 'Economic Activity', economic_acts, 'Distribution of the sample by the economic activity', "", "", False)








# print(data.groupby('Region').size()
#
# res_type = data.groupby('Residence Type')
# family_compos = data.groupby('Family Composition')
# population_base = data.groupby('Population Base')
# sex = data.groupby('Sex')
# age = data.groupby('Age')
# marital_status = data.groupby('Marital Status')
# student = data.groupby('Student')
# birth_place = data.groupby('Country of Birth')
# health = data.groupby('Health')
# ethnic_group = data.groupby('Ethnic Group')
# religion = data.groupby('Religion')
# economic_activity = data.groupby('Economic Activity')
# occupation = data.groupby('Occupation')
# industry = data.groupby('Industry')
# hours_per_week = data.groupby('Hours worked per week')
# social_grade = data.groupby('Approximated Social Grade')
