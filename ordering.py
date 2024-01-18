import pandas as pd


df = pd.read_csv('correct_merged_data.csv')
df = df[['Rank', 'Email', 'Name', 'Course', 'Year', 'Section', 'Marks', 'Time Taken']]

df.to_csv('ordered_student_data.csv', index=False)
print("Done")