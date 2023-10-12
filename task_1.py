import csv
import os


def get_rel_path(abs_path: str, file_path: str) -> str:

    """Function returns relative path to file with path 'file_path'"""

    com_path = os.path.join(os.path.commonpath([abs_path, file_path]), "")
    rel_path = abs_path.replace(com_path, "")
    return rel_path


def main(annotation_name: str, dataset_folder: str) -> None:
    path_to_file = os.path.dirname(__file__)
    with open(annotation_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for subfolder in os.listdir(dataset_folder):
            folder = os.path.join(dataset_folder, subfolder)
            for filename in os.listdir(folder):
                abs_path = os.path.join(folder, filename)
                rel_path = get_rel_path(abs_path, path_to_file)
                row = [abs_path, rel_path, subfolder]
                writer.writerow(row)


if __name__ == "__main__":
    main("annotations_1.csv", "c:\\Users\\Acer\\Documents\\py_lab_1\\dataset")
