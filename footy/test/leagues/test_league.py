import unittest

from footy.src.leagues.league import League
from footy.test_data.test_data_paths import get_season_path


class LeagueTest(unittest.TestCase):
    def test_league_name(self):
        league = League("Stuff", [])
        self.assertEquals("Stuff", league.name)

    def test_seasons(self):
        csv_paths = [
            get_season_path("Premier League", 2015, 2016),
            get_season_path("Premier League", 2014, 2015)
        ]
        league = League("something", csv_paths)
        self.assertEquals(2, len(league.seasons))

    def test_seasons_start_year(self):
        csv_paths = [
            get_season_path("Premier League", 2015, 2016),
            get_season_path("Premier League", 2014, 2015)
        ]
        league = League("Premier League", csv_paths)
        self.assertEquals(2015, league.seasons[0].start_year)
        self.assertEquals(2014, league.seasons[1].start_year)

    def test_seasons_end_year(self):
        csv_paths = [
            get_season_path("Premier League", 2015, 2016),
            get_season_path("Premier League", 2014, 2015)
        ]
        league = League("Premier League", csv_paths)
        self.assertEquals(2016, league.seasons[0].end_year)
        self.assertEquals(2015, league.seasons[1].end_year)