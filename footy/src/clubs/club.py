class Club:
    @property
    def matches(self):
        return [match for match in self._matches if match.host_name == self.name or match.visitor_name == self.name]

    def __init__(self, club_name, matches):
        self.name = club_name
        self._matches = matches
