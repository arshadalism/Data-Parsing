import csv


def convert_time_to_seconds(time_str):
    parts = time_str.split()
    total_seconds = 0

    for i in range(len(parts)):
        if parts[i] == 'mins':
            total_seconds += int(parts[i - 1]) * 60
        elif parts[i] == 'secs':
            total_seconds += int(parts[i - 1])

    return total_seconds


with open('grade_input.csv', 'r') as input_file:
    data = csv.reader(input_file)
    input_data = []
    for rec in data:
        # print(rec)
        input_data.append(rec)

    header = input_data[0]
    students_data = input_data[1:]

    # print(len(students_data))

    parsed_data = []

    for student in students_data:
        first_name = student[header.index('First name')]
        email = student[header.index('Email address')]
        marks = student[header.index('Grade/30')]
        time_taken = student[header.index('Time taken')]

        data = [first_name, email, marks, time_taken]

        parsed_data.append(data)

    sorted_data = sorted(parsed_data[0:], key=lambda x: (int(x[2]), -convert_time_to_seconds(x[3])), reverse=True)

    filtered_data = [entry for entry in sorted_data if all(field != '' for field in entry)]
    # print(filtered_data)

    for i, student in enumerate(filtered_data, start=1):
        student.insert(0, str(i))

    header = ['Rank', 'Name', 'Email', 'Marks', 'Time Taken']
    filtered_data.insert(0, header)

    with open('student_test_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(filtered_data)

print("CSV file created successfully")
