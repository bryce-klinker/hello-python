import unittest

from footy.src.seasons.season import Season
from footy.test_data.test_data_paths import get_season_path


class SeasonTest(unittest.TestCase):

    def test_start_year_matches_data_file_start_year(self):
        season_path = get_season_path("Premier League", 2015, 2016)
        season = Season(season_path)
        self.assertEquals(2015, season.start_year)

    def test_end_year_matches_data_file_end_year(self):
        season_path = get_season_path("Premier League", 2014, 2015)
        season = Season(season_path)
        self.assertEquals(2015, season.end_year)

    def test_league_name_matches_data_file_league_name(self):
        season_path = get_season_path("Premier League", 2014, 2015)
        season = Season(season_path)
        self.assertEquals("Premier League", season.league_name)

    def test_clubs_match_clubs_in_data_file(self):
        season_path = get_season_path("Premier League", 2014, 2015)
        season = Season(season_path)
        self.assertEquals(20, len(season.clubs))
