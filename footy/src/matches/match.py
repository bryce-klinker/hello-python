class Match:
    @property
    def host_name(self):
        return self.match_values[2]

    def __init__(self, match_line):
        self.match_values = match_line.split(',')