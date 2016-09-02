import os
from itertools import *

from footy.src.matches.match import Match
from footy.src.clubs.club import Club


class ClubGateway:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def get_all(self):
        csv_contents = self.read_csv()
        lines = csv_contents.split('\n')
        matches = [Match(line) for line in islice(lines, 1, None) if len(line) > 1]
        groups = groupby(sorted(matches, key=lambda m: m.host_name), lambda m: m.host_name)
        clubs = [Club(key, matches) for key, group in groups]
        return clubs

    def read_csv(self):
        f = None
        try:
            f = open(self.csv_path)
            return f.read()
        finally:
            if f is not None:
                f.close()
