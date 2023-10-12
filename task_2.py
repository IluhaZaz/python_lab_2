import csv
import os
import shutil


def main(dir_for_copy: str, dataset_dir: str, annotation_name: str) -> None:
    path_to_file = os.path.dirname(__file__)
    with open(annotation_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for subfolder in os.listdir(dataset_dir):
            for file in os.listdir(os.path.join(dataset_dir, subfolder)):
                orig_file = os.path.join(dataset_dir, subfolder, file)
                copy_file = os.path.join(dir_for_copy, subfolder + "_" + file)
                shutil.copyfile(orig_file, copy_file)
                com_path = os.path.join(
                    os.path.commonpath([path_to_file, copy_file]), ""
                )
                rel_path = copy_file.replace(com_path, "")
                row = [orig_file, rel_path, subfolder]
                writer.writerow(row)


if __name__ == "__main__":
    main(
        "c:\\Users\\Acer\\Documents\\py_lab_2\\dataset_copy_2",
        "c:\\Users\\Acer\\Documents\\py_lab_1\\dataset",
        "annotations_2.csv",
    )
