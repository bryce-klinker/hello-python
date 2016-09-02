from behave import *

from footy.src.leagues.league_gateway import LeagueGateway
from footy.test_data.test_data_paths import get_season_path, seasons_path

use_step_matcher("re")


@when("I get clubs in the (.*) for (.\d+)-(.\d+)")
def step_impl(context, league, start_year, end_year):
    season = LeagueGateway(seasons_path).get_season(league, start_year, end_year)
    context.clubs = season.clubs


@then("I should have (.\d+) clubs")
def step_impl(context, club_count):
    assert len(context.clubs) is int(club_count)


@then("I should have clubs")
def step_impl(context):
    club_names = [club.club_name for club in context.clubs]
    for row in context.table:
        assert row['club_name'] in club_names
