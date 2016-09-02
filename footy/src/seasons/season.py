from footy.src.clubs.club_gateway import ClubGateway
from footy.src.shared.data_path import get_start_year, get_end_year, get_league_name


class Season:
    @property
    def league_name(self):
        return get_league_name(self.data_path)

    @property
    def start_year(self):
        return get_start_year(self.data_path)

    @property
    def end_year(self):
        return get_end_year(self.data_path)

    @property
    def clubs(self):
        return self.club_gateway.get_all()

    def __init__(self, data_path):
        self.data_path = data_path
        self.club_gateway = ClubGateway(self.data_path)
