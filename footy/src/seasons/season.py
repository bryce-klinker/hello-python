from footy.src.shared.csv_path import get_start_year, get_end_year, get_league_name


class Season:
    @property
    def league_name(self):
        return get_league_name(self.csv_path)

    @property
    def start_year(self):
        return get_start_year(self.csv_path)

    @property
    def end_year(self):
        return get_end_year(self.csv_path)

    def __init__(self, csv_path):
        self.csv_path = csv_path
