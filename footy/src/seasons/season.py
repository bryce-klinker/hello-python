from os import path


class Season:

    @property
    def start_year(self):
        base_path = path.basename(self.csv_path)
        parts = base_path.split("_")
        return int(parts[0])

    @property
    def end_year(self):
        base_path = path.basename(self.csv_path)
        parts = base_path.split("_")
        return int(parts[1])

    def __init__(self, csv_path):
        self.csv_path = csv_path