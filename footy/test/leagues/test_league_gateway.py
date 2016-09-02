import unittest

from footy.src.leagues.league_gateway import LeagueGateway
from footy.test_data.test_data_paths import seasons_path


class LeagueGatewayTest(unittest.TestCase):
    def test_get_all_leagues_should_get_leagues_from_seasons(self):
        gateway = LeagueGateway(seasons_path)
        leagues = gateway.get_all()
        self.assertEquals(2, len(leagues))

    def test_get_all_gets_pretty_league_names(self):
        gateway = LeagueGateway(seasons_path)
        league_names = [league.name for league in gateway.get_all()]
        self.assertIn("Premier League", league_names)
        self.assertIn("Championship", league_names)