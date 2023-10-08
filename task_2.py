import csv
import os
import shutil

path_to_file = os.path.dirname(__file__)
dir_for_copy = "c:\\Users\\Acer\\Documents\\py_lab_2\\dataset_copy_2"
dataset_dir = "c:\\Users\\Acer\\Documents\\py_lab_1\\dataset"
with open("annotations_2.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    for subfolder in os.listdir(dataset_dir):
            for file in os.listdir(os.path.join(dataset_dir, subfolder)):
                orig_file = dataset_dir + "\\" + subfolder + "\\" + file
                copy_file = dir_for_copy + "\\" + subfolder + "_" + file 
                shutil.copyfile(orig_file, copy_file)
                com_path = os.path.commonpath([path_to_file, copy_file]) + "\\"
                rel_path = copy_file.replace(com_path,"")
                row = [orig_file,  rel_path, subfolder]
                writer.writerow(row)

