import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


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
    df = pd.read_csv(file_name, error_bad_lines=False)
    df = df[df['Region'].isin(
        ['E12000001', 'E12000002', 'E12000003', 'E12000004', 'E12000005',
         'E12000006', 'E12000007', 'E12000008', 'E12000009', 'W92000004'])]
    df = df[df['Residence Type'].isin(['C', 'H'])]
    df = df[df['Family Composition'].isin([1, 2, 3, 4, 5, 6, -9])]  # can change to: list(range(0, x).append(-9)
    df = df[df['Population Base'].isin([1, 2, 3])]
    df = df[df['Sex'].isin([1, 2])]
    df = df[df['Age'].isin([1, 2, 3, 4, 5, 6, 7, 8])]
    df = df[df['Marital Status'].isin([1, 2, 3, 4, 5])]
    df = df[df['Student'].isin([1, 2])]
    df = df[df['Country of Birth'].isin([1, 2, -9])]
    df = df[df['Health'].isin([1, 2, 3, 4, 5, -9])]
    df = df[df['Ethnic Group'].isin([1, 2, 3, 4, 5, -9])]
    df = df[df['Religion'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    df = df[df['Economic Activity'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    df = df[df['Occupation'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, -9])]
    df = df[df['Industry'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -9])]
    df = df[df['Hours worked per week'].isin([1, 2, 3, 4, -9])]
    df = df[df['Approximated Social Grade'].isin([1, 2, 3, 4, -9])]
    df.duplicated(['Person ID'], keep='first')
    return df


def analyse(df):
    print('Total no of records: ', df.shape[0])
    print(df.groupby('Region').size(), '\n')
    print(df.groupby('Residence Type').size(), '\n')
    print(df.groupby('Family Composition').size(), '\n')
    print(df.groupby('Population Base').size(), '\n')
    print(df.groupby('Sex').size(), '\n')
    print(df.groupby('Age').size(), '\n')
    print(df.groupby('Marital Status').size(), '\n')
    print(df.groupby('Student').size(), '\n')
    print(df.groupby('Country of Birth').size(), '\n')
    print(df.groupby('Health').size(), '\n')
    print(df.groupby('Ethnic Group').size(), '\n')
    print(df.groupby('Religion').size(), '\n')
    print(df.groupby('Economic Activity').size(), '\n')
    print(df.groupby('Occupation').size(), '\n')
    print(df.groupby('Industry').size(), '\n')
    print(df.groupby('Hours worked per week').size(), '\n')
    print(df.groupby('Approximated Social Grade').size(), '\n')


def create_bar_plot(char_type, df, column, names, title, x_axis, y_axis):
    df_size = len(df[column].unique())
    color_map = [[x / df_size, x / (df_size * 5.0), 0.2] for x in range(df_size)]
    df = df.replace({column: names})
    plot = df[column].value_counts().plot(kind=char_type, title=title, color=color_map)
    plot.set_xlabel(x_axis)
    plot.set_ylabel(y_axis)
    plt.show()


def create_pie_plot(char_type, df, column, names, title):
    df = df.replace({column: names})
    df[column].value_counts().plot(kind=char_type, title=title)
    plt.show()


def create_3d_plot(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.xticks([-9, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    plt.yticks(np.arange(10), df.index.levels[0])
    for x in range(len(df.index.levels[0])):
        xs = df[df.index.levels[0][x]]
        ax.bar(xs.index, xs.values, zs=x, zdir='y')
    plt.show()


def group(df, col1, col2):
    return df.groupby([col1, col2]).size()


data = read_csv('data')

# create_bar_plot('bar', data, 'Region', regions, 'Number of Records for each region', 'Regions', 'No. of Records')
create_3d_plot(group(data, 'Region', 'Industry'))

# analyse(d)
# create_bar_plot('bar', data, 'Occupation', occupations, 'Number of Records for each Occupation', 'Occupation', 'No. of Records')
# create_pie_plot('pie', data, 'Age', ages, 'Distribution of the sample by age')
# create_pie_plot('pie', data, 'Economic Activity', economic_acts, 'Distribution of the sample by the economic activity')
