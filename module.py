import csv

class temp ():
    def __init__(self):
        self.file = "temp.csv"
        self.fields = []
        self.rows = []

    def add_form(self,dict):
        with open(self.file, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(dict)

    def remove_form(self):
        pass

