import csv
import os

with open("annotations_1.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    main_folder = "C:\\Users\\Acer\\Documents\\py_lab_1\\dataset"
    for subfolder in os.listdir(main_folder):
        folder = os.path.join(main_folder, subfolder)
        for filename in os.listdir(folder):
            abs_path = os.path.join(folder, filename)
            row = [abs_path, os.path.join("dataset", subfolder, filename), subfolder]
            writer.writerow(row)