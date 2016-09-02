import unittest
from nose.tools import *

from footy.test_data.test_data_paths import premier_league_2015_2016_path
from footy.src.clubs.club_gateway import ClubGateway


class ClubGatewayTest(unittest.TestCase):
    def setUp(self):
        self.gateway = ClubGateway(premier_league_2015_2016_path)

    def test_get_all_clubs(self):
        clubs = self.gateway.get_all()
        self.assertEquals(20, len(clubs))

    def test_get_all_clubs_includes_club_name(self):
        clubs = self.gateway.get_all()
        self.assertEquals("Arsenal", clubs[0].club_name)
        self.assertEquals("Aston Villa", clubs[1].club_name)
        self.assertEquals("Bournemouth", clubs[2].club_name)
