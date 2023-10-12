import os

from task_4 import get_next


class Iterator:
    def __init__(self, dataset_dir: str, class_mark: str):
        self.limit = 0
        for subfolder in os.listdir(dataset_dir):
            self.limit += len(os.listdir(os.path.join(dataset_dir, subfolder)))
        self.counter = 0
        self.class_mark = class_mark
        self.dataset_dir = dataset_dir

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return get_next(self.class_mark, self.dataset_dir, self.counter - 1)
        else:
            raise StopIteration


a = Iterator(
    os.path.join("c:\\", "Users", "Acer", "Documents", "py_lab_1", "dataset"), "good"
)
for i in range(1000):
    print(next(a))