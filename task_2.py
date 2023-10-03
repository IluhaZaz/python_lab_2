import csv
import os
import shutil
 
dir_for_copy = "C:\\Users\\Acer\\Documents\\py_lab_2\\dataset_copy_2"
dataset_dir = "C:\\Users\\Acer\\Documents\\py_lab_1\\dataset"
with open("annotations_2.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    for subfolder in os.listdir(dataset_dir):
            for file in os.listdir(os.path.join(dataset_dir, subfolder)):
                orig_file = dataset_dir + "\\" + subfolder + "\\" + file
                copy_file = dir_for_copy + "\\" + subfolder + "_" + file 
                shutil.copyfile(orig_file, copy_file)
                rel_path = orig_file.replace(os.path.commonpath([orig_file, "C:\\Users\\Acer\\Documents\\py_lab_2\\task_2.py"]) + "\\","")
                row = [orig_file,  rel_path, subfolder]
                writer.writerow(row)

