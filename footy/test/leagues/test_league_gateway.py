import unittest

from footy.src.leagues.league_gateway import LeagueGateway
from footy.test_data.test_data_paths import seasons_path


class LeagueGatewayTest(unittest.TestCase):
    def setUp(self):
        self.gateway = LeagueGateway(seasons_path)

    def test_get_all_leagues_should_get_leagues_from_seasons(self):
        leagues = self.gateway.get_all()
        self.assertEquals(2, len(leagues))

    def test_get_all_gets_pretty_league_names(self):
        league_names = [league.name for league in self.gateway.get_all()]
        self.assertIn("Premier League", league_names)
        self.assertIn("Championship", league_names)

    def test_get_season_gets_season_for_league_start_and_end_year(self):
        season = self.gateway.get_season("Premier League", 2014, 2015)
        self.assertEquals("Premier League", season.league_name)
        self.assertEquals(2014, season.start_year)
        self.assertEquals(2015, season.end_year)

    def test_get_season_gets_season_for_league_string_start_year_and_string_end_year(self):
        season = self.gateway.get_season("Premier League", "2014", "2015")
        self.assertEquals(2014, season.start_year)
        self.assertEquals(2015, season.end_year)