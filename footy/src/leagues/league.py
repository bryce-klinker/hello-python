from footy.src.seasons.season import Season


class League:
    def __init__(self, league_name, csv_paths):
        self.name = league_name
        self.seasons = [Season(csv_path) for csv_path in csv_paths]
