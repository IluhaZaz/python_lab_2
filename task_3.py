import csv
import os
import shutil
from random import sample

dir_for_copy = "C:\\Users\\Acer\\Documents\\py_lab_2\\dataset_copy_3"
dataset_dir = "C:\\Users\\Acer\\Documents\\py_lab_1\\dataset"

rand_int_list = sample(list(range(1,10001)), 2000)
rand_count = 0

with open("annotations_3.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    for subfolder in os.listdir(dataset_dir):
            for file in os.listdir(os.path.join(dataset_dir, subfolder)):
                orig_file = dataset_dir + "\\" + subfolder + "\\" + file
                copy_file = dir_for_copy + "\\" + str(rand_int_list[rand_count]) 
                rand_count+=1
                shutil.copyfile(orig_file, copy_file)
                rel_path = orig_file.replace(os.path.commonpath([orig_file, "C:\\Users\\Acer\\Documents\\py_lab_2\\task_3.py"]) + "\\","")
                row = [orig_file,  rel_path, subfolder]
                writer.writerow(row)
