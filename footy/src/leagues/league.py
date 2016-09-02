from footy.src.seasons.season import Season


class League:

    @property
    def seasons(self):
        return self._seasons

    def __init__(self, league_name, csv_paths):
        self.name = league_name
        self._seasons = [Season(csv_path) for csv_path in csv_paths]
