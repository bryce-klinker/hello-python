from behave import *

from footy.src.leagues.league_gateway import LeagueGateway
from footy.test_data.test_data_paths import seasons_path

use_step_matcher("re")


@when("I get leagues")
def step_impl(context):
    context.leagues = LeagueGateway(seasons_path).get_all()


@then("I get all leagues")
def step_impl(context):
    for row in context.table:
        league = [league for league in context.leagues if league.name == row['league_name']][0]
        season = [season for season in league.seasons if season.start_year == int(row['start_year'])][0]
        assert season.end_year is int(row['end_year'])