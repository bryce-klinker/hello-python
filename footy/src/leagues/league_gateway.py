from os import listdir, path
from itertools import groupby, islice

from footy.src.leagues.league import League


class LeagueGateway:
    def __init__(self, seasons_path):
        self.seasons_path = seasons_path

    def get_all(self):
        files = [file for file in listdir(self.seasons_path)]
        file_paths = [path.realpath(path.join(self.seasons_path, file)) for file in files]
        csv_file_paths = [file_path for file_path in file_paths if path.splitext(file_path)[1] == '.csv']
        sorted_csv_paths = sorted(csv_file_paths, key=lambda csv_path: LeagueGateway.get_league_name(csv_path))
        grouped_leagues = groupby(sorted_csv_paths, lambda csv_path: LeagueGateway.get_league_name(csv_path))
        return [League(key, group) for key, group in grouped_leagues]

    @staticmethod
    def get_league_name(csv_path):
        file_name = path.basename(csv_path)
        parts = islice(file_name.split("_"), 2, None)
        league_name_with_extension = " ".join(parts)
        return league_name_with_extension.split(".")[0]