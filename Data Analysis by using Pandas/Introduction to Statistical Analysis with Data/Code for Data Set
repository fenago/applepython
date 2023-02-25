import pandas as pd

# Creating the dataset
data = {
    'PassengerId': [1, 2, 3, 4, 5],
    'Survived': [0, 1, 1, 1, 0],
    'Pclass': [3, 1, 3, 1, 2],
    'Name': ['Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
             'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
             'Allen, Mr. William Henry'],
    'Sex': ['male', 'female', 'female', 'female', 'male'],
    'Age': [22, 38, 26, 35, 35],
    'SibSp': [1, 1, 0, 1, 0],
    'Parch': [0, 0, 0, 0, 0],
    'Ticket': ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803', '373450'],
    'Fare': [7.25, 71.2833, 7.925, 53.1, 8.05],
    'Cabin': [None, 'C85', None, 'C123', None],
    'Embarked': ['S', 'C', 'S', 'S', 'S']
}

df = pd.DataFrame(data)

# Saving the dataset as a CSV file
df.to_csv('titanic.csv', index=False)
