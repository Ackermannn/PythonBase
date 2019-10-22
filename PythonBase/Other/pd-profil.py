import pandas as pd
import pandas_profiling

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
data.describe()


data.profile_report(title='Titanic Dataset')
