import csv
import os
 
path_to_file = os.path.dirname(__file__)

with open("annotations_1.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    main_folder = "c:\\Users\\Acer\\Documents\\py_lab_1\\dataset"
    for subfolder in os.listdir(main_folder):
        folder = os.path.join(main_folder, subfolder)
        for filename in os.listdir(folder):
            abs_path = os.path.join(folder, filename)
            com_path = os.path.commonpath([abs_path, path_to_file]) + "\\"
            rel_path = abs_path.replace(os.path.commonpath([abs_path, com_path]) + "\\","")
            row = [abs_path, rel_path, subfolder]
            writer.writerow(row)