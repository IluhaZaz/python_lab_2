import os


def get_next(class_mark: str, dataset_dir: str, num: int) -> str:

    """Function returns next abs path in 'dataset_dir' with class 'class_mark'"""

    for subfolder in os.listdir(dataset_dir):
        if subfolder == class_mark:
            abs_subfolder = os.path.abspath(os.path.join(dataset_dir, subfolder))
            files = os.listdir(abs_subfolder)
            return os.path.join(abs_subfolder, files[num])
    return None

