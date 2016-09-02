import unittest
from nose.tools import *

from footy.src.clubs.club_gateway import ClubGateway

class ClubGatewayTest(unittest.TestCase):
    def test_get_all_clubs(self):
        gateway = ClubGateway()
        clubs = gateway.get_all()
        self.assertEquals(20, len(clubs))