import os
from itertools import *
from operator import itemgetter

from footy.src.matches.match import Match
from footy.src.clubs.club import Club


class ClubGateway:
    def get_all(self):
        csv_contents = ClubGateway.read_csv()
        lines = csv_contents.split('\n')
        matches = [Match(line) for line in islice(lines, 1, None) if len(line) > 1]
        groups = groupby(sorted(matches, key=lambda m: m.host_name), lambda m: m.host_name)
        clubs = [Club(key, matches) for key, group in groups]
        return clubs

    @staticmethod
    def read_csv():
        f = None
        try:
            csv_path = os.path.realpath(os.path.join(__file__, '..', '..', '..', 'test_data', 'seasons', '2015_2016_Premier_League.csv'))
            f = open(csv_path)
            return f.read()
        finally:
            if f is not None:
                f.close()
