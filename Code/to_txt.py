import csv

csv_file = r'/home/mihir/WPI/Fall 22/CV/p4/YourDirectoryID_p4/Code/new.csv'
txt_file = r'ground_truth.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        reader = csv.reader(my_input_file)
        next(reader)  # skip the header
        my_output_file.write(','.join(row[0] for row in reader))