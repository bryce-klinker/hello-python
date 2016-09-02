import unittest

from footy.src.clubs.club_gateway import ClubGateway
from footy.test_data.test_data_paths import get_season_path


class ClubTest(unittest.TestCase):

    def setUp(self):
        season_path = get_season_path("Premier League", 2015, 2016)
        self.club = ClubGateway(season_path).get_all()[0]


    def test_matches_has_only_matches_with_club_as_host_or_visitor(self):
        for match in self.club.matches:
            self.assert_club_is_in_match(self.club, match)

    def assert_club_is_in_match(self, club, match):
        match_clubs = [ match.host_name, match.visitor_name ]
        self.assertIn(club.name, match_clubs)