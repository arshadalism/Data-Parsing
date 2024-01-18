import pandas as pd

file1 = "student_test_data.csv"
df1 = pd.read_csv(file1)

file2 = "Hackathon 2.csv"
df2 = pd.read_csv(file2)


df1['Email'] = df1['Email'].str.strip().str.lower()
df1['Name'] = df1['Name'].str.strip().str.upper()
df2['Email'] = df2['Email'].str.strip().str.lower()
df2['Name'] = df2['Name'].str.strip().str.upper()


df2_subset = df2[['Email', 'Name', 'Course', 'Year', 'Section']]

merged_df1 = pd.merge(df1, df2_subset, left_on=['Email', 'Name'], right_on=['Email', 'Name'], how='left')

merged_df1.drop_duplicates(inplace=True)


merged_df1.to_csv('correct_merged_data.csv', index=False)


print("Done")
