
# import pandas as pd
# f=pd.read_csv("/home/mihir/WPI/Fall 22/CV/p4/YourDirectoryID_p4/MH_01_easy/mav0/state_groundtruth_estimate0/data.csv", usecols = [0, 1, 2, 3, 5, 6, 7, 4])
# # keep_col = ['timestamp', 'p_RS_R_x [m]', 'p_RS_R_y [m]', 'p_RS_R_z [m]', 'q_RS_x []', 'q_RS_y []', 'q_RS_z []', 'q_RS_w []']
# # keep_col = [[0], 1, 2, 3, 7, 5, 6, 4]
# # new_f = f[keep_col]
# f.to_csv("newFile.csv", index=False)

# import csv

# with open('/home/mihir/WPI/Fall 22/CV/p4/YourDirectoryID_p4/MH_01_easy/mav0/state_groundtruth_estimate0/data.csv', 'r') as infile, open('reordered.csv', 'a') as outfile:
#     # output dict needs a list for new column ordering
#     fieldnames = [0, 1, 2, 3, 5, 6, 7, 4]
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#     # reorder the header first
#     writer.writeheader()
#     for row in csv.DictReader(infile):
#         # writes the reordered rows to the new file
#         writer.writerow(row)


csv_in  = open("/home/mihir/WPI/Fall 22/CV/p4/YourDirectoryID_p4/MH_01_easy/mav0/state_groundtruth_estimate0/data.csv", "r")
csv_out = open("gt.txt", "w")

for line in csv_in:
    field_list = line.split(',')    # split the line at commas
    output_line = ' '.join([field_list[0],   # rejoin with commas, new order
                           field_list[1],
                           field_list[2],
                           field_list[3],
                           field_list[5],
                           field_list[6],
                           field_list[7],
                           field_list[4] + '\n'
                           ])
    csv_out.write(output_line)

csv_in.close()
csv_out.close()


