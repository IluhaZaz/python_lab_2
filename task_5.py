from task_4 import get_next
import csv

file = "annotations_2.csv"

class Iterator:
    def __init__(self, limit, csv_file, class_mark):
        self.limit = limit
        self.counter = 0
        self.reader = csv.reader(open(csv_file))
        self.class_mark = class_mark
    
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return get_next(self.class_mark, self.reader)
        else:
            raise StopIteration
        
a = Iterator(10, file, "good")
for i in range(10):
    print(next(a))