import csv
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def main():
    file1_path = 'student_test_data.csv'
    file2_path = 'Hackathon 2.csv'

    with open(file1_path, 'r', newline='') as file1:
        reader1 = csv.reader(file1)
        data1 = list(reader1)

    with open(file2_path, 'r', newline='') as file2:
        reader2 = csv.reader(file2)
        data2 = list(reader2)

    for row2 in data2:
        matching_rows = []
        for i, row1 in enumerate(data1):
            if row1['Email'] == row2['Email'] or similar(row1['Name'], row2['Name']) > 0.8:
                matching_rows.append(i)

        for matching_row_index in matching_rows:
            data1[matching_row_index].update({
                "Course": row2['Course'],
                "Year": row2['Year'],
                "Section": row2['Section'],
            })
    with open(file1_path, 'w', newline='') as file10:
        fieldnames = ['Rank', 'Name', 'Email', 'Marks', 'Time Taken', 'Year', 'Section', 'Course']
        writer = csv.DictWriter(file10, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data1)


if __name__ == "__main__":
    main()

