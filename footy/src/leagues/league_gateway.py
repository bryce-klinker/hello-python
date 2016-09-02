from os import listdir, path
from itertools import groupby, islice

from footy.src.leagues.league import League
from footy.src.shared.csv_path import get_league_name


class LeagueGateway:
    def __init__(self, seasons_path):
        self.seasons_path = seasons_path

    def get_all(self):
        files = [file for file in listdir(self.seasons_path)]
        file_paths = [path.realpath(path.join(self.seasons_path, file)) for file in files]
        csv_file_paths = [file_path for file_path in file_paths if path.splitext(file_path)[1] == '.csv']
        sorted_csv_paths = sorted(csv_file_paths, key=lambda csv_path: get_league_name(csv_path))
        grouped_leagues = groupby(sorted_csv_paths, lambda csv_path: get_league_name(csv_path))
        return [League(key, group) for key, group in grouped_leagues]

    def get_league(self, league_name):
        return [league for league in self.get_all() if league.name == league_name][0]

    def get_season(self, league_name, start_year, end_year):
        league = self.get_league(league_name)
        return [season for season in league.seasons if season.start_year == start_year and season.end_year == end_year][0]
